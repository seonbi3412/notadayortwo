<template>
  <div class="movies">
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
      if (this.$route.params.movieName){
        this.movies = this.movies.filter(movie => movie.title === this.$route.params.movieName)
      }
    })
    .catch(error => {
      console.log(error)
    })
  },
}
</script>
