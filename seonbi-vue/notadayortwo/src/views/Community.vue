<template>
  <div class="community">
    <div id="nav">
      <router-link to="/" exact>Home</router-link> |
      <router-link to="/movies">Movies</router-link> |
      <router-link to="/account">Account</router-link> |
      <router-link to="/account/login">Login</router-link> |
      <router-link to="/account/signup">Signup</router-link> |
      <router-link to="/community">Community</router-link>
    </div>
    <h1>This is a community page</h1>
    <router-view ></router-view>
  </div>
</template>