<template>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { onMounted } from 'vue'

const router = useRouter()

onMounted(() => {
	const place = location.pathname.split("/").slice(-2)[0]
	const tank  = location.pathname.split("/").slice(-1)[0]
	const url   = "/watch/" + place + "/" + tank

    router.push(url)
})
</script>

<style scoped>
</style>