<template>
  <v-navigation-drawer image="https://cdn.vuetifyjs.com/images/backgrounds/bg-2.jpg" app location="right">

  </v-navigation-drawer>
  <div>
    <v-list-item v-for="item in items" :key="item.title" :to="item.to">
      <v-list-item-title>
        {{ item.title }}
      </v-list-item-title>
    </v-list-item>
  </div>
</template>

<script>
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Menu",
  data() {
    return {
      items: [
        {
          'title': 'home',
          'to': '/'
        }
      ]
    }
  }
}
</script>

<style scoped>

</style>