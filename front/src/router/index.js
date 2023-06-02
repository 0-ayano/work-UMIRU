import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomeView
        },
        {
            path: '/watch/:place/:tank',
            name: 'タンクの観察',
            component: () => import('../views/WatchView.vue')
        },
        {
            path: '/tmp/:place/:tank',
            name: '仲介',
            component: () => import('../views/TmpView.vue')
        },
    ]
})

export default router
