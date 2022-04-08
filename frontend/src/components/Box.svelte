<script lang="ts">
    import { createEventDispatcher } from "svelte";
    import Button from "./Button.svelte";
    import { fade } from "svelte/transition";

    const dispatch = createEventDispatcher();
    export let padding = "20px";
</script>

<div
    in:fade="{{ delay: 250 }}"
    out:fade
    class="box"
    style="{`padding: ${padding};`}">
    <div class="header">
        <Button
            id="back-button"
            color="white"
            on:click="{() => dispatch('close')}">
            Close view
        </Button>
    </div>
    <slot />
</div>

<style lang="scss">
    .box {
        background-color: white;
        border-radius: 12px;
        border: 1px solid #000000;
        height: 100%;
        box-sizing: border-box;
        overflow-y: auto;

        .header {
            text-align: right;
        }
    }
</style>
