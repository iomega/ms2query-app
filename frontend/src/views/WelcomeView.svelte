<script lang="ts">
    import Button from "../components/Button.svelte";
    import { createEventDispatcher } from "svelte";

    const dispatch = createEventDispatcher();
</script>

<div class="welcome-view">
    <h1>Welcome to ms2query App!</h1>

    <div>
        <Button
            id="run-ms2query"
            color="black"
            on:click="{() => dispatch('click', 'run')}">
            Run new ms2query session</Button>
        <Button
            id="show-process"
            color="black"
            on:click="{() => dispatch('click', 'process')}"
            >Show analysis process</Button>
        <Button
            id="show-results"
            color="black"
            on:click="{() => dispatch('click', 'analysis')}"
            >Show analysis results</Button>
    </div>
</div>

<style lang="scss">
    .welcome-view {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 8rem;
        overflow-y: auto;
    }

    h1 {
        margin: 0;
        margin-top: 5rem;
        text-decoration: underline;
        text-align: center;
    }

    div {
        display: flex;
        flex-direction: column;
        gap: 2rem;
    }
</style>
