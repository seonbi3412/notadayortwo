<template>
  <div class="search">
    <search-bar :movies="movies" :actors="actors" :genres="genres" @input-change-event="onInputChange"/>
    <MovieListItem v-for="movie in searchMovies" :key="`movie-${movie.id}`" :movie="movie" :reviews="reviews"/>
    <ActorListItem v-for="actor in searchActors" :key="actor.id" :actor="actor" :reviews="reviews"/>
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar.vue'
import MovieListItem from '@/components/movies/MovieListItem.vue'
import ActorListItem from '@/components/actors/ActorListItem.vue'

export default {
  name: "search",
  components:{
    SearchBar,
    MovieListItem,
    ActorListItem,
  },
  props: {
    movies: {
      type: Array,
      required: true
    },
    genres: {
      type: Array,
      required: true
    },
    users:{
      type: Array,
      required: true
    },
    actors:{
      type: Array,
      required: true
    },
    reviews: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      searchMovies: {},
      searchActors: {}
    }
  },
  methods: {
    onInputChange(value) {
      this.searchMovies = this.movies.filter(movie => {
        if(movie.title.includes(value)){
          return movie
        }
        let selectMovie = movie.genres.filter(genre => {
          if(genre.name.includes(value)){
            return genre
            }
        })
        if (selectMovie.length > 0){
          return selectMovie
        }
      })
      this.searchActors = this.actors.filter(actor => actor.name.includes(value))
    },
  },
  mounted() {
    if (this.$route.params.movieName){
      this.searchMovies = this.movies.filter(movie => {
        if(movie.title.includes(this.$route.params.movieName)){
          return movie
        }
        let selectMovie = movie.genres.filter(genre => {
          if(genre.name.includes(this.$route.params.movieName)){
            return genre
            }
        })
        if (selectMovie.length > 0){
          return selectMovie
        }
      })
      this.searchActors = this.actors.filter(actor => actor.name.includes(this.$route.params.movieName))
    }
    else{
      this.searchMovies = this.movies
      this.searchActors = this.actors
    }
  }
}
</script>

<style>

</style>