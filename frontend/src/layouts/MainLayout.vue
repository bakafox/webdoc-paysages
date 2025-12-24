<script setup lang="ts">
import { FileCog, ImagePlay, LayoutGrid, Terminal, TextInitial } from 'lucide-vue-next'

import { RouterView } from 'vue-router'

import SideLink from '@/components/SideLink.vue'
</script>

<template>
    <div class="layout">
        <aside>
            <h2 class="title">
                Классификация<br>пейзажей
            </h2>

            <SideLink link="/">
                <TextInitial :size="16" />
                Описание проекта
            </SideLink>
            <SideLink link="/details">
                <FileCog :size="16" />
                Технические детали
            </SideLink>
            <SideLink link="/try">
                <ImagePlay :size="16" />
                Попробовать онлайн
            </SideLink>
            <SideLink link="/history">
                <LayoutGrid :size="16" />
                История загрузок
            </SideLink>
            <SideLink link="/api">
                <Terminal :size="16" />
                API (Swagger)
            </SideLink>
            <SideLink link="https://github.com/zhabiki/paysage-classification">
                Исходный код на GitHub
            </SideLink>
        </aside>

        <main>
            <RouterView />
        </main>
    </div>
</template>

<style lang="css" scoped>
    .layout {
        flex: 1;
        display: flex; flex-direction: row;
        max-height: 100vh;
    }

    .title {
        /* text-align: center; */
        /* color: var(--accent-dark) */
        margin: 16px 0; padding: 0 12px;
    }

    aside {
        display: flex; flex-direction: column;
        padding: 16px 20px; gap: 4px;
    }

    main {
        flex: 1;
        display: flex; flex-direction: column;
    }
</style>
