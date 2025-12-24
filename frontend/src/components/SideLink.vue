<script setup lang="ts">
import { RouterLink } from 'vue-router'

const { link } = defineProps<{
    link: string,
}>()
</script>

<template>
    <RouterLink v-if="link.startsWith('/')" :to="link" class="sidelink">
        <slot />
    </RouterLink>
    <a v-else :href="link" target="_blank" class="sidelink">
        <slot />
    </a>
</template>

<style lang="css" scoped>
    .sidelink {
        display: flex; flex-direction: row;
        align-items: center; gap: 6px;
        padding: 8px 12px;
        background-color: transparent; color: var(--accent-dark);
        border-radius: var(--BR-round);
        font-weight: 600; text-decoration: none;
        transition: var(--TR-normal);

        &:hover {
            background-color: var(--white-55);

            &:active {
                background-color: var(--accent); color: var(--white);
            }
        }

        &.router-link-exact-active {
            background-color: var(--accent); color: var(--white);

            &:hover {
                background-color: var(--accent-light);

                &:active {
                    background-color: var(--accent-dark);
                }
            }
        }
    }
</style>
