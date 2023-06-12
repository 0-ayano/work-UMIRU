<template>
    <div class="frame">
        <form class="setting" @submit.prevent="submitForm">
            <input type="date" v-model="from" @change="updateToDate">
            <span>～</span>
            <input type="date" v-model="to" :min="from">
            <button class="btn" type="submit">決定</button>
        </form>

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
const from = ref('');
const to = ref('');

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

const updateToDate = () => {
    if (from.value && to.value < from.value) {
        to.value = from.value;
    }
};

const submitForm = async () => {
    if (from.value && to.value) {
        const place = location.pathname.split('/').slice(-2)[0]
        const tank = location.pathname.split('/').slice(-1)[0]
        const url = 'http://localhost:8000/graph/' + place + '/' + tank + '/' + from.value + '/' + to.value

        await axios.get(url).then((res) => {
            if (res.data.msg == "--Success--") {
                dt.value = res.data.data.map(item => item.dt)
                const columns = Object.keys(res.data.data[0]).filter(key => key !== 'dt');
                dataSets.value = columns.map(column => ({
                    name: column,
                    data: res.data.data.map(item => item[column])
                }));
                renderCharts();
            }

            else {
                dt.value = []
                dataSets.value = [[], [], [], [], []]
                renderCharts();
            }
        })
    }
};
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

.center {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    /* センターリングするための高さを指定します */
}

.setting {
    position: relative;
    margin: 5% 0 0 0;
    display: flex;
    justify-content: center;
    align-items: center;
}

.btn {
    min-width: 30%;
    height: 70%;
    color: var(--color-white);
    background-color: var(--color-blue);
    border: 0;
    cursor: pointer;
    font-size: x-large;

    position: relative;
    margin: 0 0 0 0;
    overflow: hidden;
}

input[type="date"] {
    appearance: none;
    -webkit-appearance: none;
    background-color: var(--color-white);
    border-radius: 4px;
    padding: 6px 8px;
    font-size: 14px;
    margin-right: 2%;
    margin-left: 2%;
    width: 20%;
}
</style>
  