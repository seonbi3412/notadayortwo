<template>
  <div id="nav">
      <router-link to="/" exact>Home</router-link> |
      <router-link to="/movies">Movies</router-link> |
      <router-link to="/account">Account</router-link> |
       <div v-if="!isAuthenticated">
        <router-link to="/account/login">Login</router-link> |
        <router-link to="/account/signup">Signup</router-link> |
      </div>
      <div v-else>
        <a @click.prevent="logout" href="#">Logout</a>
      </div>
      <router-link to="/community">Community</router-link>
    </div>
</template>

<script>
export default {
    name: 'Nav',
    data() {
    return {
      movies: [],
      isAuthenticated: this.$session.has('jwt'),
    }
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
  },
  mounted() {
    this.isLogin()
  },
}
</script>