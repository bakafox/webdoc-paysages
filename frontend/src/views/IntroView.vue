<script setup lang="ts">
import Page from '@/components/Page.vue'
</script>

<template>
    <Page>
        <h1>Проект «Классификация пейзажей»</h1>

        <hr>

        <img src="/img-intro.png" alt="Демонстрация пезультата работы программы">

        <p>
            Учебная задача классификации изображений, в которой необходимо
            обучить модель разделять картинки пейзажей на 6 категорий —
            <b>здания, леса, горы, ледники, улицы, и моря</b>.
        </p>

        <p>
            Датасет на Kaggle:
            <a href="https://www.kaggle.com/datasets/nitishabharathi/scene-classification">
                https://www.kaggle.com/datasets/nitishabharathi/scene-classification
            </a>
        </p>

        <p>
            Оттуда мы используем только часть Train (~17 тысяч картинок),
            поскольку в Test отсутствуют метки. В качестве нейронной сети
            для дообучения на данных используется <b>EfficientNetV2</b>.
        </p>
    </Page>
</template>
