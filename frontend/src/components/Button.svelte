<script lang="ts">
    import { createEventDispatcher } from "svelte";

    const dispatch = createEventDispatcher();

    export let id: string;
</script>

<button id="{id}" on:click="{() => dispatch('click')}">
    <slot />
</button>

<style lang="scss">
    button {
        padding: 0.5rem;
        cursor: pointer;
        background-color: #003f63;
        border: none;
        border-radius: 0.2rem;
        color: #d9d9d9;

        &:hover {
            background-color: lighten(#003f63, 10%);
        }
    }
</style>
