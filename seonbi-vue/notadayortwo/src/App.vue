<template>
  <div id="app">
    <div v-if="!this.$route.path.includes('account')">
      <Nav/>
    </div>
    <router-view/>
  </div>
</template>

<script>
// @ is an alias to /src
import Nav from './views/Nav.vue'

export default {
  name: 'app',
  components: {
    Nav
  },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
}
#nav a {
  font-weight: bold;
  color: #2c3e50;
}
#nav a.router-link-exact-active {
  color: #42b983;
}
</style>