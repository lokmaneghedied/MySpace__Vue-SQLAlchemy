import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/HomeView')
  },
  {
    path: '/newaccount',
    name: 'NewAccount',
    component: () => import('../views/NewAccount.vue')
  },
   {
    path: '/user/:email',
    name: 'User',
    component: () => import('../views/User.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
