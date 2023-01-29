<script setup>
import { onMounted } from "vue"
import { googleOneTap, googleLogout } from "vue3-google-login"
import axios from "axios"

const logOut = function (){
  googleLogout()
}

onMounted(() => {
  googleOneTap({autoLogin:true})
    .then((response) => {
      const data = {
        "access_token" : response.credential,
        "token_type" : "bearer"
      }
      // This promise is resolved when user selects an account from the the One Tap prompt
      axios.post("/auth", data).then((res)=>{
        console.log(res)
      }).catch((err)=>{
        console.log(err)
      })
      console.log("Handle the response", response)
    })
    .catch((error) => {
      console.log("Handle the error", error)
    })
})

</script>

<template>
  <v-btn @click="logOut">
    logout
  </v-btn>
</template>