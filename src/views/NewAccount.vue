<template>
  <div class="flex justify-center place-items-center font-serif bg-blue-100 min-h-screen">
    <CreateNew @goBack="goBack" @newUser="create" />
  </div>
</template>


<script>
import router from '../router'
import CreateNew from '../components/CreateNew'
export default {
  name: 'NewAccount',
  data() {
    return {
    }
  },
  components: {
    CreateNew,
  },
  methods: {
    goBack() {
      router.push({path:'/'})
    },
    create(user) {   
      router.push({ name: 'User', params:{email:user.email} })
    }
  }
}
</script>