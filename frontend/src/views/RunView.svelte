<script lang="ts">
    import FilePond, { registerPlugin, supported } from "svelte-filepond";
    import "filepond/dist/filepond.min.css";

    // a reference to the component, used to call FilePond methods
    let pond;

    // pond.getFiles() will return the active files

    // the name to use for the internal file input
    let name = "filepond";

    // handle filepond events
    function handleInit() {
        console.log("FilePond has initialised");
    }

    function handleAddFile(err, fileItem) {
        console.log("A file has been added", fileItem);
    }
</script>

<div class="run-view">
    In this view, a new ms2query analysis run can be launched after uploading an
    appropriate file.

    <div class="filepond-wrapper">
        <FilePond
            bind:this="{pond}"
            name="{name}"
            server="/api"
            allowMultiple="{true}"
            oninit="{handleInit}"
            onaddfile="{handleAddFile}" />
    </div>
</div>

<style lang="scss">
    .run-view {
        padding: 30px;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 3rem;
        text-align: center;

        .filepond-wrapper {
            width: 25rem;
        }
    }
</style>
