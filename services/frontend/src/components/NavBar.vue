<template>
  <div>
    <header>
      <a href="/"><strong>DS LOUNGE</strong></a>
      <login-component/>
    </header>
  </div>
</template>

<script>
import LoginComponent from "@/components/LoginComponent.vue";

export default {
  name: "NavBar",
  components: {LoginComponent}
}
</script>

<style scoped>

</style>