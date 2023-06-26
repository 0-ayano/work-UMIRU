<template>
    <div class="frame">
        <!-- <form class="setting" @submit.prevent="submitForm">
            <input type="date" v-model="from" @change="updateToDate">
            <span>～</span>
            <input type="date" v-model="to" :min="from">
            <button class="btn" type="submit">決定</button>
        </form> -->

        <div v-for="index in 5" :key="index" class="chart-container"></div>
    </div>
</template>
  
<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import Highcharts from 'highcharts'

const dt = ref([])
const dataSets1 = ref([])
const dataSets2 = ref([])
const categoryData = ref(["水温", "塩分", "伝導率", "Do（%）", "Do（mg/L）"])
const unit = ref(["℃", "ppt", "mS / cm", "%", "mg / L"])
const from = ref('');
const to = ref('');

onMounted(async () => {
    const place = location.pathname.split('/').slice(-2)[0]
    const tank = location.pathname.split('/').slice(-1)[0]
    const url1 = 'http://localhost:8000/first_graph_10/' + place + '/' + tank
    const url2 = 'http://localhost:8000/first_graph_15/' + place + '/' + tank

    await axios.get(url1).then((res1) => {
        dt.value = res1.data.data.map(item => item.dt).reverse();
        const columns = Object.keys(res1.data.data[0]).filter(key => key !== 'dt');
        dataSets1.value = columns.map(column => ({
            name: column,
            data: res1.data.data.map(item => item[column]).reverse()
        }));
    })

    await axios.get(url2).then((res2) => {
        dt.value = res2.data.data.map(item => item.dt).reverse();
        const columns = Object.keys(res2.data.data[0]).filter(key => key !== 'dt');
        dataSets2.value = columns.map(column => ({
            name: column,
            data: res2.data.data.map(item => item[column]).reverse()
        }));
        renderCharts();
    })

    // console.log(dataSets1.value)
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
            categories: dt.value.map((item) => formatDate(item)),
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
                dataSets1.value = columns.map(column => ({
                    name: column,
                    data: res.data.data.map(item => item[column])
                }));
                renderCharts();
            }

            else {
                dt.value = []
                dataSets1.value = [[], [], [], [], []]
                renderCharts();
            }
        })
    }
};

const formatDate = (dateString) => {
    const date = new Date(dateString);
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    const hours = String(date.getHours()).padStart(2, '0');
    const minutes = String(date.getMinutes()).padStart(2, '0');
    const seconds = String(date.getSeconds()).padStart(2, '0');

    // return `${year}年${month}月${day}日 ${hours}時${minutes}分${seconds}秒`;
    return `${year}年${month}月${day}日`;
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