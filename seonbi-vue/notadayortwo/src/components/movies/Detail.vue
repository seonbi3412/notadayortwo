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
    <h1>{{ movie.title}}</h1>
    <img :src="poster_url" :alt="movie.title">
    <h5>{{ movie.score }} | {{ movie.open_date }}</h5>
    <h5>장르: <span v-for="genre in movie.genres" :key="genre.id">{{ genre.name }} </span></h5>
    <p>{{ movie.description }}</p>
    
    
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
  },
  data() {
    return {
      poster_url: `https://image.tmdb.org/t/p/w500${this.movie.poster_url}`
    }
  }
}
</script>

<style>

</style>