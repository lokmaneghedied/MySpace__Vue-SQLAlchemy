<template>
  <div class="font-serif bg-blue-100 h-screen flex justify-center place-items-center	">
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
      router.push({ name: 'Users', params:{email:user.email} })
    }
  }
}
</script>