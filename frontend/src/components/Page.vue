<template>
    <div class="page">
        <div class="page__inner">
            <slot />
        </div>
    </div>
</template>

<style lang="css" scoped>
    .page {
        flex: 1;
        margin: 20px 20px 20px 0; padding: 16px 24px;
        max-height: 100%;
        overflow: auto;
        background-color: var(--white-99); color: var(--black);
        /* border: 1px solid var(--bg); */
        border-radius: var(--BR-normal);
    }
    .page__inner {
        min-width: 0; max-width: 800px;
        margin: auto; padding: 20px;
    }
</style>
