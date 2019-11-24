<template>
  <div class="mx-auto" style="width: 400px;" v-if="show">
    <b-form>
			<b-form-group id="input-group-1" label="Your Name:" label-for="input-1">
        <b-form-input
          id="input-1"
          v-model="form.name"
          required
          placeholder="Enter name"
        ></b-form-input>
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
					:state="validation"
          required
        ></b-form-input>
				<b-form-invalid-feedback :state="validation">
        Your password must be 8-20 characters long, contain letters and numbers, and must not
        contain spaces, special characters, or emoji.
      </b-form-invalid-feedback>
      <b-form-valid-feedback :state="validation">
        Looks Good.
      </b-form-valid-feedback>
      </b-form-group>

      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>

    </b-form>
  </div>
</template>

<script>
export default {
	name: 'UserForm',
	data() {
		return {
			form: {
				email: '',
				name: '',
				password: '',
			},
			show: true
		}
	},
	computed: {
		validation() {
			return this.form.password.includes("-")
		}
	}
}
</script>

<style>

</style>