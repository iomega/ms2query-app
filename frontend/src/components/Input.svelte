<script lang="ts">
    export let label: string | undefined = undefined;
    export let value: string = "";
</script>

<div class="search-input">
    {#if label}
        <label for="search-input">{label}:</label>
    {/if}
    <input bind:value type="text" id="search-input" name="search-input" />
</div>

<style lang="scss">
    .search-input {
    }
</style>
