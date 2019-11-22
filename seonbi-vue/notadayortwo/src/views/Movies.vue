<template>
  <div class="movies">
    <div id="nav">
      <router-link to="/" exact>Home</router-link> |
      <router-link to="/movies">Movies</router-link> |
      <router-link to="/account">Account</router-link> |
      <router-link to="/account/login">Login</router-link> |
      <router-link to="/account/signup">Signup</router-link> |
      <router-link to="/community">Community</router-link>
    </div>
    <h1>This is a movies page</h1>
    <movie-list :movies="movies"/>
  </div>
</template>

<script>
// @ is an alias to /src
import MovieList from '@/components/movies/MovieList_m.vue'
import axios from 'axios'

export default {
  name: 'movies',
  components: {
    MovieList
  },
  data() {
    return {
      movies: [],
    }
  },
  mounted() {
    axios.get(`http://127.0.0.1:8000/movies/`)
    .then(response =>{
      console.log(response.data)
      this.movies = response.data
    })
    .catch(error => {
      console.log(error)
    })
  },
}
</script>
