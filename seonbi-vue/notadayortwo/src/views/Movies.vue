<template>
  <div class="movies">
    <h1>This is a movies page</h1>
    <movie-list :movies="movies"/>
  </div>
</template>

<script>
// @ is an alias to /src
import MovieList from '@/components/movies/MovieList_m.vue'

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
    this.movies =[{title:'조커', id:1}, {title:'말레피센트', id:2}]
  },
}
</script>
