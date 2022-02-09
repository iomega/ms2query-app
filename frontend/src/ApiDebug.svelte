<script lang="ts">
    import Box from "./Box.svelte";
    import ResultsTable from "./components/ResultsTable.svelte";
    import Input from "./components/Input.svelte";
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
        <div class="table-box">
            <Input bind:value="{searchKeyword}" label="Suche" />
            <ResultsTable items="{tableItemsSearched}" />
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

    .table-box {
        display: flex;
        flex-direction: column;
        gap: 20px;
        text-align: left;
    }
</style>
