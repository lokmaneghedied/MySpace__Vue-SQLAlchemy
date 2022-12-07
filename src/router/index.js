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
    path: '/users/:email',
    name: 'Users',
    component: () => import('../views/Users.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
