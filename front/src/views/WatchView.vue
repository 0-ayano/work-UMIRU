<template>
    <current class="position_current"></current>
    <bottom class="position_bottom"></bottom>
    <graph class="position_graph"></graph>
</template>

<script setup>
import current from '../components/current_information.vue'
import bottom from '../components/bottom.vue'
import graph from '../components/graph.vue'
</script>

<style scoped>
.position_current{
    /* position: relative; */
    margin: 2% 0 0 5%;
}

.position_bottom{
    position: fix;
    bottom: 0%;
    left: 0%;
}

.position_graph{
    margin: 2% 0 0 45%;
}
</style>