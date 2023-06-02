<template>
    <div class="frame">
        <div v-for="index in 5" :key="index" class="chart-container"></div>
    </div>
</template>
  
<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import Highcharts from 'highcharts'

const dt = ref([])
const dataSets = ref([])
const categoryData = ref(["水温（℃）", "塩分（ppt）", "伝導率（mS/cm）", "Do（%）", "Do（mg/L）"])

onMounted(async () => {
    const place = location.pathname.split('/').slice(-2)[0]
    const tank = location.pathname.split('/').slice(-1)[0]
    const url = 'http://localhost:8000/first_graph/' + place + '/' + tank

    await axios.get(url).then((res) => {
        dt.value = res.data.data.map(item => item.dt).reverse();
        const columns = Object.keys(res.data.data[0]).filter(key => key !== 'dt');
        dataSets.value = columns.map(column => ({
            name: column,
            data: res.data.data.map(item => item[column]).reverse()
        }));
        renderCharts();
    })
})

const renderCharts = () => {
    const options = {
        chart: {
            type: 'line',
        },
        title: {
            text: '',
        },
        xAxis: {
            labels: {
                enabled: false, // カテゴリラベルを非表示にする
            },
            categories: dt.value,
        },
        series: [],
    }

    const chartContainers = document.querySelectorAll('.chart-container')

    if (chartContainers.length === dataSets.value.length) {
        chartContainers.forEach((container, index) => {
            options.series = [dataSets.value[index]]
            options.title.text = [categoryData.value[index]]
            Highcharts.chart(container, options)
        })
    }
}
</script>
  
<style scoped>
.frame {
    position: absolute;
    width: 50%;
    height: 75%;
    background-color: var(--color-white);
    overflow-y: scroll;
}

.chart-container {
    position: relative;
    height: 60%;
    width: 90%;

    margin-bottom: 20px;
    margin: 20px;
}
</style>
  