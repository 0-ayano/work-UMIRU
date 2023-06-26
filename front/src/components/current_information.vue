<template>
	<div class="frame">
		<img src="../assets/img/video-img.png" alt="水槽の動画" class="video">
		<div class="information">
			<table border="0">
				<tr>
					<td class="column"></td>
					<td>最新</td>
					<td>10時</td>
					<td>15時</td>
				</tr>
				<tr>
					<td class="column">水温(℃)</td>
					<td>{{ temp_current }}</td>
					<td>{{ temp_10time }}</td>
					<td>{{ temp_15time }}</td>
				</tr>
				<tr>
					<td class="column">塩分(ppt)</td>
					<td>{{ shibu_current }}</td>
					<td>{{ shibu_10time }}</td>
					<td>{{ shibu_15time }}</td>
				</tr>
				<tr>
					<td class="column">伝導度(mS/cm)</td>
					<td>{{ condact_current }}</td>
					<td>{{ condact_10time }}</td>
					<td>{{ condact_15time }}</td>
				</tr>
				<tr>
					<td class="column">DO(%)</td>
					<td>{{ do_per_current }}</td>
					<td>{{ do_per_10time }}</td>
					<td>{{ do_per_15time }}</td>
				</tr>
				<tr>
					<td class="column">DO(mg/L)</td>
					<td>{{ do_mg_current }}</td>
					<td>{{ do_mg_10time }}</td>
					<td>{{ do_mg_15time }}</td>
				</tr>
			</table>
		</div>

	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const temp_current = ref()
const shibu_current = ref()
const condact_current = ref()
const do_mg_current = ref()
const do_per_current = ref()

const temp_10time = ref()
const shibu_10time = ref()
const condact_10time = ref()
const do_mg_10time = ref()
const do_per_10time = ref()

const temp_15time = ref()
const shibu_15time = ref()
const condact_15time = ref()
const do_mg_15time = ref()
const do_per_15time = ref()


onMounted(() => {
	const place = location.pathname.split("/").slice(-2)[0]
	const tank  = location.pathname.split("/").slice(-1)[0]
	const url_current   = "http://localhost:8000/current/" + place + "/" + tank
	const url_10time   = "http://localhost:8000/10time/" + place + "/" + tank
	const url_15time   = "http://localhost:8000/15time/" + place + "/" + tank
	
	axios.get(url_current)
	.then((res) => {
		temp_current.value = res.data.temp
		shibu_current.value = res.data.shibu
		condact_current.value = res.data.condact
		do_mg_current.value = res.data.do_mg
		do_per_current.value = res.data.do_per
	})

	axios.get(url_10time)
	.then((res) => {
		temp_10time.value = res.data.temp
		shibu_10time.value = res.data.shibu
		condact_10time.value = res.data.condact
		do_mg_10time.value = res.data.do_mg
		do_per_10time.value = res.data.do_per
	})

	axios.get(url_15time)
	.then((res) => {
		temp_15time.value = res.data.temp
		shibu_15time.value = res.data.shibu
		condact_15time.value = res.data.condact
		do_mg_15time.value = res.data.do_mg
		do_per_15time.value = res.data.do_per
	})
})


</script>

<style scoped>
.frame {
	position: absolute;
	width: 35%;
	height: 75%;
	background-color: var(--color-white);
}

.video {
	position: relative;
	width: 100%;
	left: 50%;
	transform: translateX(-50%);
}

.information {
	position: relative;
	width: 100%;
	left: 50%;
	transform: translateX(-50%);
}

.information td {
	margin: 0 0 0 0;
	font-size: 100%;
	width: 10%;
	text-align: center;
}

.information tr{
	width: 100%;
}

.column{
	text-align: center;
}
</style>