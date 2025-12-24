import { createRouter, createWebHistory } from 'vue-router'

import MainLayout from '@/layouts/MainLayout.vue'
import DetailsView from '@/views/DetailsView.vue'
import HistoryInfoView from '@/views/HistoryInfoView.vue'
import HistoryListView from '@/views/HistoryListView.vue'
import InferView from '@/views/InferView.vue'
import IntroView from '@/views/IntroView.vue'
import SwaggerView from '@/views/SwaggerView.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            component: MainLayout,
            children: [
                {
                    path: '',
                    name: 'intro',
                    component: IntroView,
                },
                {
                    path: 'details',
                    name: 'details',
                    component: DetailsView,
                },
                {
                    path: 'try',
                    name: 'infer',
                    component: InferView,
                },
                {
                    path: 'history',
                    name: 'history-list',
                    component: HistoryListView,
                },
                {
                    path: 'history/:id',
                    name: 'history-info',
                    component: HistoryInfoView,
                },
                {
                    path: 'api',
                    name: 'swagger',
                    component: SwaggerView,
                },
            ],
        },
    ],
})

export default router
