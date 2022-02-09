<script lang="ts">
    import Sidebar from "./components/Sidebar.svelte";
    import Box from "./components/Box.svelte";
    import ResultsTable from "./components/ResultsTable.svelte";
    import Input from "./components/Input.svelte";
    import { getResults } from "./api/fetch.api";
    import { fade } from "svelte/transition";

    let tableItems = [];
    $: console.log("tableItems: ", tableItems);

    let searchKeyword = "";

    $: tableItemsSearched = tableItems.filter((item) =>
        searchKeyword.length > 0
            ? Object.values(item).join(",").includes(searchKeyword)
            : true
    );

    const getDataFromApi = async () => {
        const response = await getResults();
        const data = await response.json();

        tableItems = data.map((item) => {
            return {
                ...item,
            };
        });
    };

    let files: any[] = [];
    const getLocalData = async () => {
        const file = files[0];

        tableItems = JSON.parse(await file.text());
    };
</script>

<main>
    <Sidebar />

    <div class="content">
        <Box>
            {#if tableItems.length === 0}
                <div class="upload-area">
                    <h1>
                        Um Daten anzeigen zu lassen, wählen Sie eine der beiden
                        Optionen!
                    </h1>

                    <div>
                        <button
                            id="get-data-button"
                            on:click="{() => getDataFromApi()}">
                            Daten von API abfragen
                        </button>
                    </div>

                    <h2>oder</h2>

                    <div>
                        <label for="file-upload">
                            Lokale JSON-Datei laden:
                        </label>
                        <input
                            id="file-upload"
                            type="file"
                            bind:files
                            on:change="{() => getLocalData()}" />
                    </div>
                    <div class="no-data-placeholder">
                        <img
                            src="../src/assets/Artificial Intelligence_Monochromatic.png"
                            alt="" />
                    </div>
                </div>
            {:else}
                <div class="table-box" transition:fade>
                    <Input bind:value="{searchKeyword}" label="Suche" />
                    <ResultsTable items="{tableItemsSearched}" />
                </div>
            {/if}
        </Box>
    </div>
</main>

<style lang="scss">
    :root,
    :global(body) {
        padding: 0;
        margin: 0;
        background-color: #f0f0f0;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
            Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
    }

    $sidebarWidth: 250px;
    :global(.sidebar) {
        width: $sidebarWidth;
    }

    .content {
        box-sizing: border-box;
        margin-left: $sidebarWidth;
        padding: 30px;
        height: 100vh;
        color: #353d40;

        .header {
            width: 100%;
            display: flex;
            justify-content: space-between;
        }

        .upload-area {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 20px;
            text-align: center;
        }

        .no-data-placeholder {
            text-align: center;
            img {
                height: 30rem;
                width: 30rem;
            }
        }

        .table-box {
            display: flex;
            flex-direction: column;
            gap: 20px;
            text-align: left;
        }
    }

    /* Color Theme Swatches in Hex */
    $LOFT-REDUX-LMC-1-hex: #353d40;
    $LOFT-REDUX-LMC-2-hex: #d9d9d9;
    $LOFT-REDUX-LMC-3-hex: #a1a5a6;
    $LOFT-REDUX-LMC-4-hex: #f2b138;
    $LOFT-REDUX-LMC-5-hex: #003f63;
</style>
