<template>
  <div class="mx-auto" style="width: 400px;" v-if="show">
  <div id="second">
    <div class="myform form ">
      <div class="logo mb-3">
        <div class="col-md-12 text-center">
          <h1 >회원 정보 수정</h1>
        </div>
      </div>
      <form @submit.prevent="userEdit" name="registration">
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
        <b-button type="submit" variant="primary">Next</b-button>
      <b-button :to="`/account/profile/${this.user.user_id}`" variant="danger">뒤로가기</b-button>

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
	name: 'edit',
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
    movies: {
      type: Array,
      required: true
    },
    genres: {
      type: Array,
      required: true
    },
    users:{
      type: Array,
      required: true
    },
    actors:{
      type: Array,
      required: true
    },
  },
	computed: {
    nameValidation() {
      for(let idx in this.users){
        if(this.users[idx].username === this.form.username && this.users[idx].id !== this.user.user_id){
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
    userEdit() {
      if (this.passwordValidation && this.nameValidation){
        axios.post(`http://127.0.0.1:8000/accounts/update/${this.user.user_id}/`, this.form, this.options)
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
  },
  mounted(){
    this.form.username = this.user.username
    this.form.email = this.user.email
  }
}
</script>

<style>
</style>