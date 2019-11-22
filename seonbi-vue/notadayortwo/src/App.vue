<template>
  <div id="app">
    <div id="nav">
      <router-link to="/" exact>Home</router-link> |
      <router-link to="/movies">Movies</router-link> |
      <router-link to="/account">Account</router-link> |
      <router-link to="/account/login">Login</router-link> |
      <router-link to="/account/signup">Signup</router-link> |
      <router-link to="/community">Community</router-link>
    </div>
    <router-view/>
  </div>
</template>

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
