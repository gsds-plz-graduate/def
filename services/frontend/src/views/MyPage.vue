<template>
  <v-card>
    <v-card-title v-text="user.name"/>
  </v-card>
</template>
<script>
import {defineComponent} from 'vue';

// Components

export default defineComponent({
  name: 'MyPage',
  components: {},
  data: () => ({
    user: {}
  }),
  async created() {
    await this.$store.dispatch("viewMe");
    this.user = this.$store.getters.stateUser;
  },
  methods: {
  }
});
</script>