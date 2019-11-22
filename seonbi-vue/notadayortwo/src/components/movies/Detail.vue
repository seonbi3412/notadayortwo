<template>
  <div class="detail">
    <div id="nav">
      <router-link to="/" exact>Home</router-link> |
      <router-link to="/movies">Movies</router-link> |
      <router-link to="/account">Account</router-link> |
      <router-link to="/account/login">Login</router-link> |
      <router-link to="/account/signup">Signup</router-link> |
      <router-link to="/community">Community</router-link>
    </div>
    <h1>This is a {{ movie.title}} page</h1>
    
  </div>
</template>

<script>

export default {
  name: "detail",
  props: {
    movie: {
      type: Object,
      required: true
    }
  }
}
</script>

<style>

</style>