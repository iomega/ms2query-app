<script lang="ts">

  let message:string = ""

  async function handleRequest() {
    const response = await fetch('/api/ping');
    message = (await response.json()).message;
  }

  async function getResults() {
    const response = await fetch('/api/get_results/MMV_POSITIVE');
    console.log('response: ', response);
    message = (await response.json());

  }

  async function startMs2query() {
    void (await fetch('/api/run_ms2query'));
  }
</script>

<main>
  <button on:click="{() => handleRequest()}">Ping</button>
  <p>
    {message}
  </p>

  <button on:click="{() => startMs2query()}">Start ms2query test</button>
  
  <button on:click="{() => getResults()}">get results</button>
  <p>
    {message}
  </p>


</main>

<style lang="scss">
  :root {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
      Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  }

  main {
    text-align: center;
    padding: 1em;
    margin: 0 auto;
  }
</style>
