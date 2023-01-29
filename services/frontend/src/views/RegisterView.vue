<template>
  <v-text-field required v-model="member.email" type="email"></v-text-field>
  <v-text-field required v-model="member.username" type="text"></v-text-field>
  <v-text-field required v-model="member.name" type="text"></v-text-field>
  <v-text-field required v-model="member.student_number" type="text"></v-text-field>
  <v-btn outlined @click="joinRequest">register</v-btn>
</template>
<script>
import {defineComponent} from 'vue';

// Components

export default defineComponent({
  name: 'RegisterView',
  components: {},
  data: () => ({
    member:{
      email: '',
      username: '',
      name: '',
      student_number:''
    }
  }),
  methods: {
    joinRequest(){
      if(this.$refs.form.validate()){
      }
    }
  }
});
</script>