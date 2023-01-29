<template>
<section>
</section>
</template>

<script>
import { defineComponent } from 'vue';

// Components

export default defineComponent({
  name: 'HomeView',
  components: {},
  computed :{
    isLoggedIn: function() {
      return this.$store.getters.isAuthorized;
    }
  }
});
</script>
