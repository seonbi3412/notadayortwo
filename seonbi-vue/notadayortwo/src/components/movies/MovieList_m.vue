<template>
  <div class="movielist_m">
    <MovieListItem v-for="movie in movies" :key="movie.id" :movie="movie"/>
  </div>
</template>

<script>
import MovieListItem from './MovieListItem.vue'

export default {
  name: "movieList_m",
  components:{
    MovieListItem
  },
  props: {
    movies: {
      type: Array,
      required: true
    }
  }
}
</script>

<style>

</style>
