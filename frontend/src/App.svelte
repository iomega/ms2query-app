<script lang="ts">
    import ApiDebug from "./ApiDebug.svelte";
    import Sidebar from "./Sidebar.svelte";
</script>

<!-- <Sidebar/> -->

<div class="content">
    <ApiDebug />
</div>

<style lang="scss">
    :root,
    :global(body) {
        padding: 0;
        margin: 0;
        background-color: #f0f0f0;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
            Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
    }

    .content {
        box-sizing: border-box;
        // margin-left: 250px;
        padding: 30px;
        height: 100vh;
        color: #353d40;
    }

    /* Color Theme Swatches in Hex */
    $LOFT-REDUX-LMC-1-hex: #353d40;
    $LOFT-REDUX-LMC-2-hex: #d9d9d9;
    $LOFT-REDUX-LMC-3-hex: #a1a5a6;
    $LOFT-REDUX-LMC-4-hex: #f2b138;
    $LOFT-REDUX-LMC-5-hex: #003f63;
</style>
