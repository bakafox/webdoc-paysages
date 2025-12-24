<script setup lang="ts">
import type { ClassifierResults } from '@/types/classifier'
import type { FormMessage } from '@/types/forms'

import { ref } from 'vue'

import Button from '@/components/Button.vue'
import MsgBox from '@/components/MsgBox.vue'
import ResultsChart from '@/widgets/ResultsChart.vue'

const msg = ref<FormMessage | null>(null)
const img = ref<File>()
const res = ref<ClassifierResults | null>(null)

function updateImage(e: Event | null) {
    const t = e?.target as HTMLInputElement

    if (t && t.files && t.files[0]) {
        img.value = t.files[0]
        msg.value = null
    }
    else {
        msg.value = { variant: 'error', text: 'Картинка не загрузилась!' }
    }
}

async function classifyImage() {
    res.value = null

    msg.value = { variant: 'regular', text: 'Обработка картинки, подождите…' }

    try {
        await new Promise(resolve => setTimeout(resolve, 1500))

        const mockData: ClassifierResults = {
            buildings: 0.12,
            forests: 0.05,
            glacier: 0.03,
            mountains: 0.72,
            sea: 0.02,
            street: 0.06,
        }

        // throw new Error()

        msg.value = null
        res.value = mockData
    }
    catch (err) {
        msg.value = { variant: 'error', text: 'Произошла чудовищная ошибка!!!' }
    }
}
</script>

<template>
    <div class="infer">
        <h1>Inference your balls NOW!</h1>

        <p>
            Ниже вы можете попробовать загрузить картинку
            в модель, чтобы онлайн протестировать, как
            модель её классифицирует. Обратите внимание, что
            всего модель имеет 6 выходных классов, поэтому,
            если картинку нельзя отнести ни к одному из них,
            результаты получатся не очень :)
        </p>

        <div class="controls">
            <input type="file" @change="(e) => updateImage(e)">

            <Button :disabled="!img" @click="classifyImage()">
                Поехали!
            </Button>
        </div>

        <MsgBox :msg="msg" />

        <div v-if="res" class="results">
            <h2>Результаты классификации</h2>

            <p>
                Наведите мышкой на столбец графика, чтобы увидеть точность
            </p>

            <ResultsChart :res="res" />
        </div>
    </div>
</template>

<style lang="css" scoped>
    .infer {
        flex: 1;
        display: flex; flex-direction: column;
        justify-content: center; align-items: center;
        max-width: 640px;
        margin: auto;
    }

    .results {
        width: 100%;
        margin-top: 12px; padding: 20px 20px 12px;
        background-color: var(--white-CC);
        border-radius: var(--BR-normal);
        text-align: center;
    }

    .controls {
        display: flex; flex-direction: row;
        align-items: center; gap: 8px;
        margin: 8px 0;
    }
</style>
