<template>
<div class="container">
  <div class="row">
    <div class="col-md-5 mx-auto">
      <div id="first">
        <div class="myform form ">
          <div class="logo mb-3">
            <div class="col-md-12 text-center">
            <h1>Login</h1>
            </div>
          </div>
          <form @submit.prevent="login" method="post" name="login">
            <div class="form-group">
              <label for="exampleInputEmail1">Username</label>
              <input type="username" name="username"  class="form-control" id="username" placeholder="Enter Username" v-model="credentials.username" required>
            </div>
            <div class="form-group">
              <label for="exampleInputEmail1">Password</label>
              <input type="password" name="password" id="password"  class="form-control" placeholder="Enter Password" v-model="credentials.password" required>
            </div>
            <div class="form-group">
              <p class="text-center">By bye</p>
            </div>
            <div class="col-md-12 text-center ">
              <button type="submit" class=" btn btn-block mybtn btn-primary tx-tfm">Login</button>
            </div>
            <div class="form-group">
              <p class="text-center">아직? <router-link to="/account/signup" id="signup">친구하기!</router-link></p>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import axios from 'axios'
import router from '../../router'
export default {
  name: "Login",
  data(){
      return{
          credentials: {
          }
      }
  },
  methods: {
    login() {
      axios.post('http://127.0.0.1:8000/api-token-auth/', this.credentials)
        .then(response => {
          console.log(response)
          const token = response.data.token
          this.$session.start()
          this.$session.set('jwt', token)
          // vuex actions 호출 -> dispatch
          this.$store.dispatch('login', token)
          this.credentials = {}
          this.$bvModal.hide('modal-1')
          this.$emit('redataload', true)
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