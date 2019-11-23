<template>
  <div class="movies">
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
    <h1>This is a movies page</h1>
    <movie-list :movies="movies"/>
    <router-view />
  </div>
</template>

<script>
// @ is an alias to /src
import MovieList from '@/components/movies/MovieList_m.vue'
import { mapGetters } from 'vuex'
import axios from 'axios'
import router from '../router'

export default {
  name: 'movies',
  components: {
    MovieList
  },
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
      router.push('/')
    }
  },
  computed: {
    ...mapGetters([
      'options',
      'user'
    ])
  },
  updated() {
    this.isAuthenticated = this.$session.has('jwt')
  },
  mounted() {
    this.isLogin()
    axios.get(`http://127.0.0.1:8000/movies/`, this.options)
    .then(response =>{
      console.log(response.data)
      this.movies = response.data
      if (this.$route.params.movieName){
        console.log(this.$route.params.movieName)
        this.movies = this.movies.filter(movie => movie.title === this.$route.params.movieName)
      }
    })
    .catch(error => {
      console.log(error)
    })
  },
}
</script>
