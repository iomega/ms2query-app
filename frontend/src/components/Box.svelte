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
    <div class="content">
        <slot />
    </div>
</div>

<style lang="scss">
    .box {
        background-color: white;
        border-radius: 12px;
        border: 1px solid #000000;
        height: 100%;
        box-sizing: border-box;
        overflow-y: auto;
        display: flex;
        flex-direction: column;

        .header {
            text-align: right;
            flex: 0;
        }

        .content {
            flex: 1;
        }

        /* Works on Firefox */
        scrollbar-width: thin;
        scrollbar-color: #f0f0f0 #000000;

        /* Works on Chrome, Edge, and Safari */
        &::-webkit-scrollbar {
            width: 15px;
            border-radius: 50%;
        }

        &::-webkit-scrollbar-track {
            // background: #e9e9e9;
            background: #f0f0f0;
            border-radius: 12px;
            margin: 3px 0;
        }

        &::-webkit-scrollbar-thumb {
            background-color: #000000;
            border-radius: 20px;
            border: 2px solid #f0f0f0;
        }
    }
</style>
