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

    const loadTableData = async () => {
        const response = await getResults();
        const data = await response.json();

        tableItems = data.map((item) => {
            return {
                ...item,
            };
        });
    };
</script>

<div>
    <Box>
        <div class="header">ms2query App</div>
    </Box>

    <Box>
        {#if tableItems.length > 0}
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
                <div class="table-head">smiles</div>
                <div class="table-head">cf_superclass</div>
                <div class="table-head">cf_class</div>
                <div class="table-head">cf_subclass</div>

                {#each tableItemsSearched as item, index}
                    <div class="table-data right"><b>{index + 1}</b></div>
                    <div class="table-data left">{item.smiles}</div>
                    <div class="table-data center">{item.cf_superclass}</div>
                    <div class="table-data center">{item.cf_class}</div>
                    <div class="table-data center">{item.cf_subclass}</div>
                {/each}
            </div>
        {:else}
            <button on:click="{() => loadTableData()}">
                Load Table Data
            </button>
        {/if}
    </Box>
</div>

<style lang="scss">
    .header {
        width: 100%;
        display: flex;
        justify-content: space-between;
    }

    .search-input {
        margin-bottom: 20px;
        text-align: left;
    }
    .table {
        display: grid;
        grid-template-columns: auto 1fr 1fr 1fr 1fr;
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
