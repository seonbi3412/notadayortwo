<template>
  <div class="movies">
    <h1>영화 목록 </h1>
    <movie-list :movies="movies" :genres="genres" :users="users" :actors="actors" :reviews="reviews"/>
    <router-view @redataload="loadDBdata"/>
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
    }
  },
  methods: {
    loadDBdata() {
      this.$emit('redataload', true)
    }
  }
}
</script>

<style>
</style>