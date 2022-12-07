<template>
  <div class="flex justify-around font-serif bg-blue-100 h-screen ">
    <div class="container place-self-center w-1/3">
      <h1 class="text-blue-600 text-8xl m-8 font-black"> MySpace </h1>
      <p class="text-2xl m-8">Take this opportunity to express </p>
    </div>
    <div class="container p-2 m-8 place-self-center w-1/3 bg-white rounded-xl shadow-2xl divide-y-2">
      <LogIn @user="logIn" />
      <div class="p-2 flex justify-center">
        <button class="p-3 m-4 w-2/3 rounded-lg bg-green-500 text-center text-white cursor-pointer font-bold" @click="createNewAccount" >Create New Account</button>
      </div>
    </div>
  </div>
</template>

<script>
import LogIn from '../components/LogIn'
import router from '../router'
export default {
  name: 'HomeView',
  components: {
    LogIn,
  },
  methods: {
    createNewAccount() {
      router.push({ path:'/newaccount'})
    },
    logIn(user) {
      router.push({name:'Users', params:{email:user.email}})
    }
  }
}
</script>
