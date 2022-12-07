<template>
  <router-view/>
  <Footer />
</template>

<script>
import Footer from './components/Footer'
export default {
  name: "App",
  components: {
    Footer
  }
}
</script>

<style>
</style>
