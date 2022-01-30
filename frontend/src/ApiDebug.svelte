<script lang="ts">
    import Box from "./Box.svelte";
    import { getResults } from "./fetch.api";

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

<div>
    <Box>
        <div class="header">ms2query App</div>
    </Box>

    <Box>
        <div class="upload-area">
            <div>
                <label for="get-data-button">Daten von API abfragen: </label>
                <button
                    id="get-data-button"
                    on:click="{() => getDataFromApi()}">
                    Los geht's!
                </button>
            </div>
            <div>
                <label for="file-upload">Lokale JSON-Datei laden:</label>
                <input
                    id="file-upload"
                    type="file"
                    bind:files
                    on:change="{() => getLocalData()}" />
            </div>
        </div>
    </Box>

    <Box>
        <div class="search-input">
            <label for="search-input">Suche:</label>
            <input
                bind:value="{searchKeyword}"
                type="text"
                id="search-input"
                name="search-input" />
        </div>

        <div class="table">
            <div class="table-head">No.</div>
            <div class="table-head">match_parent_mass</div>
            <div class="table-head">smiles</div>
            <div class="table-head">cf_superclass</div>
            <div class="table-head">cf_class</div>
            <div class="table-head">cf_subclass</div>

            {#each tableItemsSearched as item, index}
                <div class="table-data right"><b>{index + 1}</b></div>
                <div class="table-data left">{item.match_parent_mass}</div>
                <div class="table-data left">{item.smiles}</div>
                <div class="table-data center">{item.cf_superclass}</div>
                <div class="table-data center">{item.cf_class}</div>
                <div class="table-data center">{item.cf_subclass}</div>
            {/each}
        </div>
    </Box>
</div>

<style lang="scss">
    .header {
        width: 100%;
        display: flex;
        justify-content: space-between;
    }

    .upload-area {
        display: flex;
        justify-content: space-around;
    }

    .search-input {
        margin-bottom: 20px;
        text-align: left;
    }
    .table {
        display: grid;
        grid-template-columns: auto 1fr 1fr 1fr 1fr 1fr;
        max-height: 80vh;
        overflow: auto;
        // border: 1px solid #003f638a;
        border-radius: 12px;

        .table-head,
        .table-data {
            padding: 10px 20px;
        }

        .table-head {
            background-color: #003f63;
            color: white;
            position: sticky;
            top: 0;
        }

        .table-data {
            border-bottom: 1px solid #003f638a;
            display: flex;
            align-items: center;

            &.left {
                justify-content: left;
            }

            &.center {
                justify-content: center;
            }

            &.right {
                justify-content: right;
            }
        }
    }
</style>
