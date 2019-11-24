<template>
  <div class="signup">
    <h1>This is a signup page</h1>
    <UserForm />
  </div>
</template>


<script>
import axios from 'axios'
import UserForm from './UserForm.vue'
import router from '../../router'

export default {
  name: "Signup",
  components: {
    UserForm
  },
  methods: {
    login(credentials) {
      axios.post('http://127.0.0.1:8000/api-token-auth/', credentials)
      .then(response => {
        console.log(response)
        const token = response.data.token
        this.$session.start()
        this.$session.set('jwt', token)
        // vuex actions 호출 -> dispatch
        this.$store.dispatch('login', token)
        router.push('/')
      })
      .catch(error => {
        console.log(error)
      })
    }
  }
}
</script>

<style>
  
</style>