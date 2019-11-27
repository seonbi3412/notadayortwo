<template>
<div class="mx-auto" style="width: 400px;" v-if="show">
  <div id="second">
    <div class="myform form ">
      <div class="logo mb-3">
        <div class="col-md-12 text-center">
          <h1 >Signup</h1>
        </div>
      </div>
      <form @submit.prevent="userSignup" name="registration">
        <div class="form-group">
          <label for="username">이름</label>
          <input v-model="form.username" :state="nameValidation" type="username"  name="username" class="form-control" id="username" placeholder="Enter Username" required>
          <b-form-invalid-feedback :state="nameValidation">
            영문, 숫자, "@, ., +, -, _"을 포함하는 2-50자 가능
          </b-form-invalid-feedback>
          <b-form-valid-feedback :state="nameValidation">
            괜찮은 이름이네!
          </b-form-valid-feedback>
        </div>
        <div class="form-group">
          <label for="email">메일주소</label>
          <input v-model="form.email" type="email" name="email"  class="form-control" id="email" placeholder="Enter Email" required>
        </div>
        <div class="form-group">
          <label for="password">비밀번호</label>
          <input v-model="form.password" :state="passwordValidation" type="password" name="password" id="password"  class="form-control" placeholder="Enter Password">
          <b-form-invalid-feedback :state="passwordValidation">
            영문, 숫자를 포함해서 8-20자(특수 문자 O, 공백 문자 X)
          </b-form-invalid-feedback>
          <b-form-valid-feedback :state="passwordValidation">
            훌륭해!
          </b-form-valid-feedback>
        </div>
        <div class="col-md-12 text-center mb-3">
          <button type="submit" class=" btn btn-block mybtn btn-primary tx-tfm">함께하기</button>
        </div>
        <div class="col-md-12 ">
          <div class="form-group">
            <p class="text-center">벌써? <router-link to="/account/login">아는 척 하기</router-link></p>
          </div>
        </div>
      </form>
    </div>
  </div>
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
    userSignup() {
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