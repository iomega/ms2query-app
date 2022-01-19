<script lang="ts">
import ApiDebug from "./ApiDebug.svelte";
import Sidebar from "./Sidebar.svelte";


</script>

<!-- <Sidebar/> -->

<div class="content">

    <ApiDebug></ApiDebug>

</div>

<style lang="scss">
  :root, :global(body) {
    padding: 0;
    margin: 0;
    background-color: #F0F0F0;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
      Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  }

  .content {
    box-sizing: border-box;
    // margin-left: 250px;
    padding: 30px;
    height: 100vh;
    color: #353D40;
  }

  /* Color Theme Swatches in Hex */
  $LOFT-REDUX-LMC-1-hex: #353D40;
  $LOFT-REDUX-LMC-2-hex: #D9D9D9;
  $LOFT-REDUX-LMC-3-hex: #A1A5A6;
  $LOFT-REDUX-LMC-4-hex: #F2B138;
  $LOFT-REDUX-LMC-5-hex: #003F63;

</style>
