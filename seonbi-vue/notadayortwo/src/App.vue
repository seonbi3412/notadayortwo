<template>
  <div id="app" class="text-dark">
    <div v-if="!this.$route.path.includes('/account/login') && !this.$route.path.includes('/account/signup')">
      <Nav :genres="genres" :users="users" :actors="actors" />
    </div>
    <router-view :genres="genres" :movies="movies" :users="users" :actors="actors" />
  </div>
</template>

<script>
// @ is an alias to /src
import Nav from './views/Nav.vue'
import { mapGetters } from 'vuex'
import axios from 'axios'

export default {
  name: 'app',
  components: {
    Nav
  },
  data() {
    return {
      movies: [],
      genres: [],
      users: [],
      actors: [],
    }
  },
  computed: {
    ...mapGetters([
      'options',
      'user'
    ])
  },
  mounted() {
    axios.get(`http://127.0.0.1:8000/movies/`)
    .then(response =>{
      this.movies = response.data
    })
    .catch(error => {
      console.log(error)
    })

    axios.get(`http://127.0.0.1:8000/movies/genres/`)
    .then(response =>{
      this.genres = response.data
    })
    .catch(error => {
      console.log(error)
    })

    axios.get(`http://127.0.0.1:8000/movies/users/`)
    .then(response =>{
      this.users = response.data
    })
    .catch(error => {
      console.log(error)
    }),
    axios.get(`http://127.0.0.1:8000/movies/actors/`)
    .then(response =>{
      this.actors = response.data
    })
    .catch(error => {
      console.log(error)
    })
  },
}
</script>

<style>
#app {
  font-family: '배달의민족 한나는 열한살', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
</style>