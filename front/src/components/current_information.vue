<template>
	<div class="frame">
		<img src="../assets/img/video-img.png" alt="水槽の動画" class="video">
		<div class="information">
			<table border="0">
				<tr>
					<td class="column">水温</td>
					<td>{{ temp }}</td>
				</tr>
				<tr>
					<td class="column">塩分</td>
					<td>{{ shibu }}</td>
				</tr>
				<tr>
					<td class="column">伝導度</td>
					<td>{{ condact }}</td>
				</tr>
				<tr>
					<td class="column">DO</td>
					<td>{{ do_per }}</td>
				</tr>
				<tr>
					<td class="column"></td>
					<td>{{ do_mg }}</td>
				</tr>
			</table>
		</div>

	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const temp = ref()
const shibu = ref()
const condact = ref()
const do_mg = ref()
const do_per = ref()


onMounted(() => {
	const place = location.pathname.split("/").slice(-2)[0]
	const tank  = location.pathname.split("/").slice(-1)[0]
	const url   = "http://localhost:8000/current/" + place + "/" + tank
	
	axios.get(url)
	.then((res) => {
		temp.value = res.data.temp + " ℃"
		shibu.value = res.data.shibu + " ppt"
		condact.value = res.data.condact + " mS/cm"
		do_mg.value = res.data.do_mg + " mg/L"
		do_per.value = res.data.do_per + " %"
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
	width: 80%;
	margin: 5% 0 0 0;
	left: 50%;
	transform: translateX(-50%);
}

.information {
	position: relative;
	margin: 2% 0 0 0;
	width: 70%;
	left: 50%;
	transform: translateX(-50%);
}

.information td {
	margin: 0 0 0 0;
	font-size: 150%;
	width: 10%;
}

.column{
	text-align: center;
}
</style>