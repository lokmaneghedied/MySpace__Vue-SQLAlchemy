<template>
  <div class="grid font-serif bg-blue-100 min-h-screen lg:flex lg:justify-around">
    <div class="container place-self-center lg:w-1/3">
      <h1 class="text-blue-600 text-5xl m-8 font-black lg:text-8xl"> MySpace </h1>
      <p class="m-9 lg:text-2xl">Take this opportunity to express </p>
    </div> 
    <div class="container w-3/4 p-2 m-8 place-self-center bg-white rounded-xl shadow-2xl divide-y-2 lg:w-1/3">
      <LogIn @user="logIn" />
      <div class="p-2 flex justify-center">
        <button class="p-3 m-4  rounded-lg bg-green-500 text-center text-white cursor-pointer font-bold lg:w-2/3" @click="createNewAccount" >Create New Account</button>
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
      router.push({name:'User', params:{email:user.email}})
    }
  }
}
</script>
