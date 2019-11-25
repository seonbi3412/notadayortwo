<template>
  <div class="mx-auto" style="width: 400px;" v-if="show">
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
      <b-button type="reset" variant="danger">Reset</b-button>

    </b-form>
  </div>
</template>

<script>
import router from '../../router'
import axios from 'axios'
import { mapGetters } from 'vuex'
export default {
	name: 'UserForm',
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
	computed: {
    nameValidation() {
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
            router.push('/')
          })
          .catch(error => {
            console.log(error)
          })
      }
    }
  }
}
</script>

<style>

</style>