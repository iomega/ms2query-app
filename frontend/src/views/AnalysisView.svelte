<script lang="ts">
    import Button from "../components/Button.svelte";
    // import Box from "../components/Box.svelte";
    import ResultsTable from "../components/ResultsTable.svelte";
    import Input from "../components/Input.svelte";
    import { getResults } from "../api/fetch.api";
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

<div class="analysis-view">
    {#if tableItems.length === 0}
        <div class="upload-area">
            To see an analysis of your data, choose one of the following
            options:

            <div class="options">
                <Button
                    id="get-data-button"
                    color="black"
                    on:click="{() => getDataFromApi()}">
                    Daten von API abfragen
                </Button>
                <input
                    id="file-upload"
                    type="file"
                    bind:files
                    on:change="{() => getLocalData()}" />
            </div>
        </div>
    {:else}
        <div class="table-box" transition:fade>
            <Input bind:value="{searchKeyword}" label="Suche" />
            <ResultsTable items="{tableItemsSearched}" />
        </div>
    {/if}
</div>

<style lang="scss">
    .analysis-view {
        padding: 30px;

        .upload-area {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 3rem;
            text-align: center;

            .options {
                display: flex;
                align-items: center;
                gap: 2rem;
            }
        }

        .table-box {
            display: flex;
            flex-direction: column;
            gap: 20px;
            text-align: left;
        }
    }
</style>
