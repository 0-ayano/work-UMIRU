<template>
    <div class="frame">
        <button class = "btn" 
                v-for = "(name, index) in btn_name"
                @click = "movePage(index)"
                :style="{ backgroundColor: name === nowPT ? 'var(--color-orange)' : 'var(--color-blue)' }"
        >{{ name }}</button>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { ref, onMounted } from 'vue'
import axios from 'axios'

const router = useRouter()
const btn_name = ref([])
const place =  ref([])
const tank  = ref([])

const nowPT = ref(location.pathname.split("/").slice(-2)[0] + "_" + location.pathname.split("/").slice(-1)[0])

const movePage = (index) => {
    router.push('/tmp/' + place.value[index] + '/' + tank.value[index])
}

onMounted(() => {	
	axios.get("http://127.0.0.1:8000/table")
    .then((res) => {
        for(var i = 0; i < res.data.data.length; i++){
            btn_name.value.push( res.data.data[i]["Tables_in_umiru"] )
            place.value.push( res.data.data[i]["Tables_in_umiru"].split("_").slice(-2)[0] )
            tank.value.push( res.data.data[i]["Tables_in_umiru"].split("_").slice(-1)[0] )
        }
    });
})
</script>

<style scoped>
.frame {
	position: absolute;
	width: 100%;
	height: 15%;
	background-color: var(--color-white);

    overflow-x: scroll;
    display: flex;
}

::-webkit-scrollbar {
    height: 10px;
}
::-webkit-scrollbar-thumb {
  background-color: var(--color-blue);
  border-radius: 100pt;
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
    top: 50%;
    transform: translateY(-50%);
    margin: 0 2% 0 2%;
    overflow: hidden;
}
</style>


<!-- 
    Reference
    - [スクロールバーのデザインと表示方法をカスタマイズ！CSS完全ガイド | Designup](https://designup.jp/css-scrollbar.html)
 -->