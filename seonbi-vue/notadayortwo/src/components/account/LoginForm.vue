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
export default {
    name: "LoginForm",
    data(){
        return{
            credentials: {
            }
        }
    },
    methods: {
        login() {
            this.$emit('login-event', this.credentials)
            this.credentials = {}
        }
    }
}
</script>

<style>
</style>