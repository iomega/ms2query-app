<script lang="ts">
    import Button from "../components/Button.svelte";
    // import Box from "../components/Box.svelte";
    import ResultsTable from "../components/ResultsTable.svelte";
    import Input from "../components/Input.svelte";
    import {
        getResultById,
        getResultsFull,
        getResultsMin,
    } from "../api/fetch.api";
    import { fade } from "svelte/transition";
    import { onMount } from "svelte";

    let tableItems = [];
    $: console.log("tableItems: ", tableItems);

    let searchKeyword = "";

    $: tableItemsSearched = tableItems.filter((item) =>
        searchKeyword.length > 0
            ? Object.values(item).join(",").includes(searchKeyword)
            : true
    );

    const getDataFromApi = async (id: string) => {
        const response = await getResultById(id);
        const { data } = await response.json();
        console.log("data: ", data[0]);

        tableItems = data[0].results.analog_search.map((item) => {
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

    let previewItems = [];

    onMount(async () => {
        const response = await getResultsMin();
        const { data } = await response.json();
        previewItems = data;
    });
</script>

<div class="analysis-view">
    {#if tableItems.length === 0}
        <div class="preview-items">
            {#if previewItems.length > 0}
                The following ms2query analysis items are stored in your
                database and can be retrieved:
                <table>
                    {#each previewItems as { _id, filename, timestamp }}
                        <tr>
                            <th>
                                <Button
                                    color="black"
                                    id="{'show-' + _id + '-button'}"
                                    on:click="{() => getDataFromApi(_id)}"
                                    >Show</Button>
                            </th>
                            <th class="right">
                                <div>
                                    Filename: {filename}
                                </div>
                                <div>
                                    Date: {new Date(
                                        timestamp
                                    ).toLocaleDateString()}
                                </div>
                            </th>
                        </tr>
                    {/each}
                </table>
            {:else}
                Sorry, you have not yet any ms2query analysis items stored in
                your database.
            {/if}
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
        height: 100%;
        box-sizing: border-box;
        padding: 30px;

        .preview-items {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 3rem;
            text-align: center;

            table {
                border-collapse: separate;
                border-spacing: 0 2rem;
                th {
                    &.right {
                        text-align: left;
                        padding-left: 2rem;
                    }
                }
            }
        }

        .table-box {
            height: 100%;
            display: flex;
            flex-direction: column;
            gap: 2.5rem;
            text-align: left;

            :global(.results-table) {
                flex: 1;
            }
        }
    }
</style>
