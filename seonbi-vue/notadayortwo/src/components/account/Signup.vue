<template>
  <div class="mx-auto" style="width: 400px;" v-if="show">
    <h1>회원 가입</h1>
    <b-form @submit.prevent="userSinup">
			<b-form-group id="input-group-1" label="Your Name:" label-for="input-1">
        <b-form-input
          id="input-1"
          v-model="form.username"
          :state="nameValidation"
          required
          placeholder="Enter name"
        ></b-form-input>
        <b-form-invalid-feedback :state="nameValidation">
          Your name must be 2-50 characters long, contain letters and numbers, "@, ., +, -, _" and must not
          contain spaces, special characters, or emoji.
        </b-form-invalid-feedback>
        <b-form-valid-feedback :state="nameValidation">
          Looks Good.
        </b-form-valid-feedback>
      </b-form-group>

			<b-form-group id="input-group-2" label="Email address:" label-for="input-2" description="We'll never share your email with anyone else.">
        <b-form-input
          id="input-2"
          v-model="form.email"
          type="email"
          required
          placeholder="Enter email"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-3" label="Password:" label-for="input-3">
        <b-form-input
          id="input-3"
					type="password"
          v-model="form.password"
					:state="passwordValidation"
          required
        ></b-form-input>
				<b-form-invalid-feedback :state="passwordValidation">
          Your password must be 8-20 characters long, contain letters and numbers, and must not
          contain spaces, special characters, or emoji.
        </b-form-invalid-feedback>
        <b-form-valid-feedback :state="passwordValidation">
          Looks Good.
        </b-form-valid-feedback>
      </b-form-group>

      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button to="/" variant="danger">취소</b-button>

    </b-form>
  </div>
</template>

<script>
import router from '../../router'
import axios from 'axios'
import { mapGetters } from 'vuex'
export default {
	name: 'Signup',
	data() {
		return {
			form: {
				username: '',
        email: '',
				password: '',
			},
			show: true
		}
  },
  props: {
    genres: {
      type: Array,
      required: true
    },
    users:{
      type: Array,
      required: true
    },
  },
	computed: {
    nameValidation() {
      for(let idx in this.users){
        if(this.users[idx].username === this.form.username){
          return false
        }
      }
      const nameReg = /^([0-9a-zA-Z@.+\-_]){2,50}/
      return nameReg.test(this.form.username)
    },
		passwordValidation() {
      const passwordReg = /^[0-9]+$/
      if (this.form.password.includes(" ") ||
      (this.form.password.length < 8 || this.form.password.length > 20) ||
      passwordReg.test(this.form.password)){
        return false
      }
			return true
		},
    ...mapGetters([
      'options',
      'user'
    ])
  },
  methods: {
    userSinup() {
      if (this.passwordValidation && this.nameValidation){
        axios.post('http://127.0.0.1:8000/accounts/signup/', this.form)
          .then(response => {
            console.log(response)
            const credentials = {
              username: this.form.username,
              password: this.form.password
            }
            axios.post('http://127.0.0.1:8000/api-token-auth/', credentials)
              .then(response => {
                console.log(response)
                const token = response.data.token
                this.$session.start()
                this.$session.set('jwt', token)
                // vuex actions 호출 -> dispatch
                this.$store.dispatch('login', token)
                this.$emit('redataload', true)
                this.$bvModal.hide('modal-2')
                router.push({
                  name: 'concern',
                  params: {genres:this.genres, users:this.users}
                })
              })
              .catch(error => {
                console.log(error)
              })
          })
      }
    }
  }
}
</script>

<style>

</style>