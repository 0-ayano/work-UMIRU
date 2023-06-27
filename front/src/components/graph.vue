<template>
    <div class="frame">
        <div v-for="index in 5" :key="index" class="chart-container"></div>
    </div>
</template>
  
<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import Highcharts from 'highcharts'

const dataSets1 = ref([])
const dataSets2 = ref([])
const categoryData = ref(["水温", "塩分", "伝導率", "Do（%）", "Do（mg/L）"])
const unit = ref(["℃", "ppt", "mS / cm", "%", "mg / L"])
const from = ref('')
const to = ref('')
const date = ref()

onMounted(async () => {
    const place = location.pathname.split('/').slice(-2)[0]
    const tank = location.pathname.split('/').slice(-1)[0]
    const url1 = 'http://localhost:8000/first_graph_10/' + place + '/' + tank
    const url2 = 'http://localhost:8000/first_graph_15/' + place + '/' + tank

    await axios.get(url1).then((res1) => {
        const columns = Object.keys(res1.data.data[0]);
        dataSets1.value = columns.map(column => ({
            name: column,
            data: res1.data.data.map(item => item[column]).reverse()
        }));
    })

    await axios.get(url2).then((res2) => {
        const columns = Object.keys(res2.data.data[0]);
        dataSets2.value = columns.map(column => ({
            name: column,
            data: res2.data.data.map(item => item[column]).reverse()
        }));
    })

    var len = dataSets1.value[0].data.length
    var tmp1 = [
        { name: 'date', data: [] },
        { name: 'time', data: [] },
        { name: 'temp', data: [] },
        { name: 'shibu', data: [] },
        { name: 'condact', data: [] },
        { name: 'do_per', data: [] },
        { name: 'do_mg', data: [] }
    ];

    var tmp2 = [
        { name: 'date', data: [] },
        { name: 'time', data: [] },
        { name: 'temp', data: [] },
        { name: 'shibu', data: [] },
        { name: 'condact', data: [] },
        { name: 'do_per', data: [] },
        { name: 'do_mg', data: [] }
    ];
    
    while (dataSets1.value[0].data.length != 0 || dataSets2.value[0].data.length != 0) {
        if (dataSets1.value[0].data.length == 0) {
            tmp2[0].data.push(dataSets2.value[0].data[0])
            tmp1[0].data.push(dataSets2.value[0].data[0])
            dataSets2.value[0].data.shift()
            for (var j = 1; j < dataSets2.value.length; j++) {
                tmp2[j].data.push(dataSets2.value[j].data[0])
                tmp1[j].data.push(null)
                dataSets2.value[j].data.shift()
            }
        }

        if (dataSets2.value[0].data.length == 0) {
            tmp1[0].data.push(dataSets1.value[0].data[0])
            tmp2[0].data.push(dataSets1.value[0].data[0])
            dataSets1.value[0].data.shift()
            for (var j = 1; j < dataSets1.value.length; j++) {
                tmp1[j].data.push(dataSets1.value[j].data[0])
                tmp2[j].data.push(null)
                dataSets1.value[j].data.shift()
            }
        }

        else if (new Date(dataSets1.value[0].data[0]) < new Date(dataSets2.value[0].data[0])) {
            tmp1[0].data.push(dataSets1.value[0].data[0])
            tmp2[0].data.push(dataSets1.value[0].data[0])
            dataSets1.value[0].data.shift()
            for (var j = 1; j < dataSets1.value.length; j++) {
                tmp1[j].data.push(dataSets1.value[j].data[0])
                tmp2[j].data.push(null)
                dataSets1.value[j].data.shift()
            }
        }

        else if (new Date(dataSets1.value[0].data[0]) > new Date(dataSets2.value[0].data[0])) {
            tmp2[0].data.push(dataSets2.value[0].data[0])
            tmp1[0].data.push(dataSets2.value[0].data[0])
            dataSets2.value[0].data.shift()
            for (var j = 1; j < dataSets2.value.length; j++) {
                tmp2[j].data.push(dataSets2.value[j].data[0])
                tmp1[j].data.push(null)
                dataSets2.value[j].data.shift()
            }
        }

        else {
            for (var j = 0; j < dataSets2.value.length; j++) {
                tmp1[j].data.push(dataSets1.value[j].data[0])
                tmp2[j].data.push(dataSets1.value[j].data[0])
                dataSets1.value[j].data.shift()
                dataSets2.value[j].data.shift()
            }
        }
    }

    date.value = tmp1.find(item => item.name === 'date').data
    dataSets1.value = tmp1.filter(item => item.name !== 'time' && item.name !== 'date')
    dataSets2.value = tmp2.filter(item => item.name !== 'time' && item.name !== 'date')

    renderCharts();
})

const renderCharts = () => {
    const options = {
        chart: {
            type: 'column',
        },
        title: {
            text: '',
        },
        xAxis: {
            labels: {
                // enabled: false,
            },
            categories: date.value
        },
        yAxis: {
            title: {
                text: ''
            },
        },
        series: [],
    }

    const chartContainers = document.querySelectorAll('.chart-container')

    if (chartContainers.length === dataSets1.value.length) {
        chartContainers.forEach((container, index) => {
            options.series = [{
                name: "10時",
                data: dataSets1.value[index].data
            },
            {
                name: "15時",
                data: dataSets2.value[index].data
            }];
            options.title.text = [categoryData.value[index]]
            options.yAxis.title.text = [unit.value[index]]
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