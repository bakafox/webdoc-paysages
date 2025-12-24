<script setup lang="ts">
import type { BarSeriesOption } from 'echarts/charts'

import type {
    DatasetComponentOption,
    GridComponentOption,
    TooltipComponentOption,
    VisualMapComponentOption,
} from 'echarts/components'
import type { ComposeOption } from 'echarts/core'
import type { ClassifierResults } from '@/types/classifier'
import { BarChart } from 'echarts/charts'
import {
    DatasetComponent,
    GridComponent,
    TooltipComponent,
    VisualMapComponent,
} from 'echarts/components'
import { use } from 'echarts/core'
import { CanvasRenderer } from 'echarts/renderers'
import { ref } from 'vue'

import VChart from 'vue-echarts'

const { res } = defineProps<{
    res: ClassifierResults,
}>()

use([
    DatasetComponent,
    TooltipComponent,
    GridComponent,
    VisualMapComponent,
    BarChart,
    CanvasRenderer,
])

type EChartsOption = ComposeOption<
    | DatasetComponentOption
    | TooltipComponentOption
    | GridComponentOption
    | VisualMapComponentOption
    | BarSeriesOption
>

const options = ref<EChartsOption>({
    dataset: {
        source: [
            ['label', 'score'],
            ...Object.entries(res),
        ],
    },
    tooltip: {
        trigger: 'axis',
        axisPointer: { type: 'shadow' },
    },
    grid: {
        left: '0px',
        right: '0px',
        top: '20px',
        bottom: '20px',
    },
    yAxis: {
        type: 'value',
        // axisLabel: { show: false },
    },
    xAxis: {
        type: 'category',
        axisLabel: { show: false },
    },
    visualMap: {
        show: false,
        min: 0.1,
        max: 0.9,
        dimension: 1,
        inRange: {
            color: ['#FD665F', '#FFCE34', '#65B581'],
        },
    },
    series: [
        {
            type: 'bar',
            encode: {
                y: 'score',
                x: 'label',
            },
            label: {
                show: true,
                position: 'bottom',
                formatter: '{b}',
            },
        },
    ],
})
</script>

<template>
    <section class="chart">
        <VChart class="chart__inner" :option="options" autoresize />
    </section>
</template>

<style lang="css" scoped>
    .chart {
        /* flex: 1; */
        width: 100%; height: 320px;
    }
</style>
