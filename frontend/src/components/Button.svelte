<script lang="ts">
    import { createEventDispatcher } from "svelte";

    const dispatch = createEventDispatcher();

    export let id: string;
    export let color: "white" | "black" | "blue";
</script>

<button id="{id}" class="{color}" on:click="{() => dispatch('click')}">
    <slot />
</button>

<style lang="scss">
    button {
        font-family: "IBM Plex Mono", monospace;
        padding: 0.75rem;
        cursor: pointer;
        border: none;
        border-radius: 0.2rem;

        &.white {
            background-color: #ffffff;
            color: #000000;

            &:hover {
                background-color: darken(#ffffff, 25%);
            }
        }

        &.black {
            background-color: #000000;
            color: #ffffff;

            &:hover {
                background-color: lighten(#000000, 75%);
            }
        }

        &.blue {
            background-color: #003f63;
            color: #d9d9d9;

            &:hover {
                background-color: lighten(#003f63, 10%);
            }
        }
    }
</style>
