<script lang="ts">
    export let padding= "20px";
</script>

<div class="box" style={`padding: ${padding};`}>
    <slot/>
</div>

<style lang="scss">
    .box {
        background-color: white;
        border-radius: 12px;
        margin-bottom: 20px;
        text-align: center;
    }
</style>