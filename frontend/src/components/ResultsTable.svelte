<script lang="ts">
    interface TableItem {
        match_parent_mass: any;
        smiles: any;
        cf_superclass: any;
        cf_class: any;
        cf_subclass: any;
    }

    export let items: Array<TableItem> = [];
</script>

<div class="results-table">
    <div class="table-head">No.</div>
    <div class="table-head">match_parent_mass</div>
    <div class="table-head">smiles</div>
    <div class="table-head">cf_superclass</div>
    <div class="table-head">cf_class</div>
    <div class="table-head">cf_subclass</div>

    {#each items as item, index}
        <div class="table-data right">
            <b>{index + 1}</b>
        </div>

        <div class="table-data left">
            {item.match_parent_mass}
        </div>

        <div class="table-data left">
            <div class="svg-wrapper">
                {@html item.smiles}
            </div>
        </div>

        <div class="table-data center">
            {item.cf_superclass}
        </div>

        <div class="table-data center">
            {item.cf_class}
        </div>

        <div class="table-data center">
            {item.cf_subclass}
        </div>
    {/each}
</div>

<style lang="scss">
    .results-table {
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

        .svg-wrapper {
            border: 1px solid #000;
            height: 200px;
            width: 200px;
            padding: 5px;
            display: flex;
            align-items: center;
            justify-content: center;
            word-break: break-all;

            svg {
                width: 100%;
                height: auto;
            }
        }
    }
</style>
