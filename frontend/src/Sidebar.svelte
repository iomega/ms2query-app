<script lang="ts">
</script>

<div class="sidebar">
    <div class="header">ms2query-app</div>

    <div class="nav-item active">Welcome</div>

    <div class="nav-item">Navigation 1</div>

    <div class="nav-item">Navigation 2</div>

    <div class="nav-item">Navigation 3</div>
</div>

<style lang="scss">
    .sidebar {
        position: fixed;
        top: 0;
        bottom: 0;
        left: 0;
        text-align: center;
        width: 250px;
        box-sizing: border-box;
        background-color: #353d40;
        color: #ffffff;
    }

    .header {
        font-size: 20px;
        font-weight: 700;
        margin-bottom: 30px;
        padding: 30px;
        border-bottom: 1px solid #f0f0f0;
    }

    .nav-item {
        padding: 10px;
        margin-bottom: 10px;
        cursor: pointer;

        &.active,
        &:hover {
            background-color: #003f63;
        }
    }
</style>
