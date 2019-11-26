<template>
  <div>
    <b-navbar type="dark" variant="dark">
      <b-navbar-brand class="col-1" to="/" exact>Home</b-navbar-brand>
      <b-navbar-nav class="col-7">
        <b-nav-item to="/movies">Movies</b-nav-item>
        <b-nav-item to="/community">Community</b-nav-item>
      </b-navbar-nav>
      <b-navbar-nav class="col-3">
        <b-nav-form v-if="this.$route.name !== 'search'" @submit.prevent="onInputChange">
          <b-form-input class="mr-sm-2" placeholder="Search"></b-form-input>
          <b-button variant="secondary" class="my-2 my-sm-0" type="submit">Search</b-button>
        </b-nav-form>
      </b-navbar-nav>
      <b-navbar-nav v-if="!isAuthenticated" class="col-1">
        <b-nav-item to="/account/login">Login</b-nav-item>
        <b-nav-item to="/account/signup">Signup</b-nav-item>
        </b-navbar-nav>
      <b-navbar-nav v-else class="col-1">
        <b-nav-item to="/account/profile">{{this.user.username}}</b-nav-item>
        <b-nav-item @click.prevent="logout" href="#">Logout</b-nav-item>
      </b-navbar-nav>
    </b-navbar>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
    name: 'Nav',
    data() {
    return {
      movies: [],
      isAuthenticated: this.$session.has('jwt'),
    }
  },
  props:{
    genres:{
      type: Array,
      required: true
    },
    users:{
      type: Array,
      required: true
    },
  },
  methods: {
    isLogin() {
      this.$session.start()
      if (this.$session.has('jwt')) {
        this.$store.dispatch('login', this.$session.get('jwt'))
      }
    },
    logout() {
      this.$session.destroy()
      this.$store.dispatch('logout')
      this.isAuthenticated = this.$session.has('jwt')
    },
    onInputChange(event) {
      console.log(event.target[0].value)
      var router = this.$router
      router.push({
        name: 'search',
        params: {movieName:event.target[0].value}
      })
    },
  },
  computed: {
    ...mapGetters([
      'options',
      'user'
    ])
  },
  mounted() {
    this.isLogin()
  },
}
</script>