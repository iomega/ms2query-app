<script lang="ts">
    import Box from "./components/Box.svelte";
    import Button from "./components/Button.svelte";
    import WelcomeView from "./views/WelcomeView.svelte";
    import AnalysisView from "./views/AnalysisView.svelte";
    import ProcessView from "./views/ProcessView.svelte";
    import RunView from "./views/RunView.svelte";

    let activeView: "welcome" | "run" | "process" | "analysis" = "welcome";
</script>

<main>
    <div class="header">
        <div class="header-left">ms2query | App</div>
        <div class="header-right">
            <Button id="about-button" color="white">About</Button>
            <Button
                id="github-button"
                color="white"
                on:click="{() =>
                    window
                        .open(
                            'https://github.com/iomega/ms2query-app',
                            '_blank'
                        )
                        .focus()}">GitHub</Button>
        </div>
    </div>

    <div class="content">
        {#if activeView === "welcome"}
            <WelcomeView on:click="{({ detail }) => (activeView = detail)}" />

            <!-- <div class="illustration">
                <img
                    src="../src/assets/Artificial Intelligence_Monochromatic.png"
                    alt="" />
            </div> -->
        {:else if activeView === "run"}
            <Box on:close="{() => (activeView = 'welcome')}">
                <RunView />
            </Box>
        {:else if activeView === "process"}
            <Box on:close="{() => (activeView = 'welcome')}">
                <ProcessView />
            </Box>
        {:else if activeView === "analysis"}
            <Box on:close="{() => (activeView = 'welcome')}">
                <AnalysisView />
            </Box>
        {/if}
    </div>
</main>

<style lang="scss">
    :root,
    :global(body) {
        padding: 0;
        margin: 0;
        color: #3f3f3f;
        background-color: #ffffff;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
            Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
        font-family: "IBM Plex Mono", monospace;
    }

    main {
        display: flex;
        flex-direction: column;
        position: fixed;
        top: 0;
        bottom: 0;
        left: 0;
        right: 0;
    }

    .header {
        flex: 0;

        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px 30px;
        box-sizing: border-box;
        height: 100px;

        .header-right {
            display: flex;
            gap: 10px;
        }
    }

    .content {
        flex: 1;
        box-sizing: border-box;
        padding: 30px;
        min-height: 0;

        .illustration {
            margin-top: 3rem;
            text-align: center;
            img {
                height: 30rem;
                width: 30rem;
            }
        }
    }

    /* Color Theme Swatches in Hex */
    $LOFT-REDUX-LMC-1-hex: #353d40;
    $LOFT-REDUX-LMC-2-hex: #d9d9d9;
    $LOFT-REDUX-LMC-3-hex: #a1a5a6;
    $LOFT-REDUX-LMC-4-hex: #f2b138;
    $LOFT-REDUX-LMC-5-hex: #003f63;
</style>
