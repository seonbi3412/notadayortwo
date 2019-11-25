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

export default {
  name: 'movies',
  components: {
    MovieList
  },
  props: {
    movies: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
    }
  },
}
</script>
