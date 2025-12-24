<script setup lang="ts">
import { RouterView } from 'vue-router'
</script>

<template>
    <RouterView />
</template>

<style>
    html {
        display: flex;
        width: 100%; height: 100%;
        margin: 0;
        font-size: 16px;
    }
    body, #app {
        flex: 1;
        display: flex; flex-direction: column;
        min-width: 100%; min-height: 100%;
        margin: 0;
        font-family: var(--fonts);
        background: var(--bg-fancy), var(--bg); color: var(--black);
    }

    h1, h2, h3 {
        margin: 0;
    }
    p, ol, ul {
        margin: 8px 0;
        line-height: 1.5;
    }
    code, pre {
        width: fit-content;
        margin: 0; padding: 2px 8px;
        background-color: var(--black); color: var(--white);
        border-radius: var(--BR-normal);
    }
    hr {
        border: 1px solid var(--accent-dark);
        margin: 4px 0 16px;
    }
</style>
