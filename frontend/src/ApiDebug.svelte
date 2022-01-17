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
  
  

  <div>
  
        <button on:click="{() => handleRequest()}">Ping</button>
        <p>
          {message}
        </p>
      
        <button on:click="{() => startMs2query()}">Start ms2query test</button>
        
        <button on:click="{() => getResults()}">get results</button>
        <p>
          {message}
        </p>
  
  </div>
  
  <style lang="scss">
  </style>
  