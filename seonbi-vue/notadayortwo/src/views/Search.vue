<template>
  <div class="search">
    <search-bar @input-change-event="onInputChange"/>
    <MovieListItem v-for="movie in searchMovies" :key="movie.id" :movie="movie"/>
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar.vue'
import MovieListItem from '@/components/movies/MovieListItem.vue'

export default {
  name: "search",
  components:{
    SearchBar,
    MovieListItem
  },
  props: {
    movies: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      searchMovies: {}
    }
  },
  methods: {
    onInputChange(value) {
      this.searchMovies = this.movies.filter(movie => movie.title === value)
    },
  },
  mounted() {
    if (this.$route.params.movieName){
      this.searchMovies = this.movies.filter(movie => movie.title === this.$route.params.movieName)
    }
    else{
      this.searchMovies = this.movies
    }
  }
}
</script>

<style>

</style>