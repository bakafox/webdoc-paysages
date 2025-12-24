from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import io
from datetime import date
from PIL import Image
import numpy as np
import torch
from torchvision import transforms
import torchvision.models as models

app = FastAPI()

# CORS для React на localhost:5173
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

image_classes = ["Buildings", "Forests", "Mountains",
"Glacier", "Street","Sea"]
history = []

@app.get('api/infer')
async def infer_image(width: int, height: int, file: UploadFile = File(..., description="Изображение для инференса")):
    try:
        # Проверка типа файла
        if not file.content_type.startswith('image/'):
            raise HTTPException(status_code=400, detail="Только изображения")
        
        # Чтение изображения
        contents = await file.read()
        image = Image.open(io.BytesIO(contents)).convert('RGB')
        
        # Преобразование для модели
        preprocess = transforms.Compose([
            transforms.ToTensor(),
            transforms.Resize([width, height]), # Ориг. разрешение: [150, 150]
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406], 
                std=[0.229, 0.224, 0.225]
            )
        ])
        
        input_tensor = preprocess(image)
        input_batch = input_tensor.unsqueeze(0)
        
        # Инференс
        if torch.cuda.is_available():
            input_batch = input_batch.to('cuda')
            model.to('cuda')
        
        with torch.no_grad():
            output = model(input_batch)
        
        # Получение вероятностей
        probabilities = torch.nn.functional.softmax(output[0], dim=0)
        
        # Создание списка с классами и вероятностями
        predictions = [
            {"class": image_classes[i], "probability": float(probabilities[i])}
            for i in range(len(image_classes[i]))
        ]
        
        # Сортировка по убыванию вероятностей
        predictions.sort(key=lambda x: x["probability"], reverse=True)

        history.append({"id": len(history) + 1, "image": image, "predictions": predictions, "datetime": date.now().isoformat()})
        
        return JSONResponse(content={
            "predictions": predictions  # Топ-10 для краткости
        })
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка инференса: {str(e)}")

@app.get('api/history')
async def get_history_and_first_page():
    page_number = np.ceil(len(history)/6)

    first_page = history[:6]

    return {"pages": page_number, "first": first_page}

@app.get('api/history/{pid}')
async def get_history_page(pid: int) -> List[dict]:
    """
    pid — номер страницы (1, 2, 3, ...).
    Возвращает массив элементов истории или [] если страницы нет.
    """
    if pid < 0:
        # Можно строго вернуть [] вместо ошибки, но так аккуратнее
        return []

    start = pid * 6
    end = start + 6

    # Если start >= len(HISTORY_DATA) — такой страницы нет, вернётся [].
    page_items = history[start:end]

    return page_items

@app.get('api/image/{hash}')
async def get_image_by_hash(hash: int):
    return history[hash]