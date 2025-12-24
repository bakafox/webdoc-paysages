<script setup lang="ts">
import type { FormMessage } from '@/types/forms'

const { msg } = defineProps<{
    msg: FormMessage | null,
}>()
</script>

<template>
    <div v-show="msg !== null" class="msgbox" :class="[msg?.variant]">
        {{ msg?.text }}
    </div>
</template>

<style lang="css" scoped>
    .msgbox {
        padding: 8px;
        border: 1px solid transparent; border-radius: var(--BR-normal);
    }
    .error {
        background-color: color-mix(in srgb, var(--error), var(--white-99) 80%);
        color: var(--error);
    }
    .success {
        background-color: color-mix(in srgb, var(--success), var(--white-99) 80%);
        color: var(--success);
    }
    .regular {
        background-color: var(--white-CC);
        color: color-mix(in srgb, var(--white-CC), var(--black) 80%);
    }
</style>
