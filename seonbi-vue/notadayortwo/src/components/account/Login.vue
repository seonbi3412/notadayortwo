<template>
  <div class="mx-auto" style="width: 400px;">
    <b-form @submit.prevent="login">
			<b-form-group id="input-group-1" label="user name :" label-for="input-1">
        <b-form-input
          id="input-1"
          v-model="credentials.username"
          required
          placeholder="Enter name"/>
      </b-form-group>

      <b-form-group id="input-group-2" label="Password :" label-for="input-2">
        <b-form-input
          id="input-2"
					type="password"
          v-model="credentials.password"
          required />
      </b-form-group>
			<b-button type="submit">로그인</b-button>
    </b-form>
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