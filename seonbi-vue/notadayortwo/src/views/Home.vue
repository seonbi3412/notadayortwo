<template>
  <div class="home">
    <search-bar :movies="movies" @input-change-event="onInputChange"/>
    <movie-list :movies="movies"/>
  </div>
</template>

<script>
// @ is an alias to /src
import SearchBar from '@/components/SearchBar.vue'
import MovieList from '@/components/home/MovieList_h.vue'

export default {
  name: 'home',
  components: {
    SearchBar,
    MovieList
  },
  data() {
    return {
    }
  },
  props: {
    movies: {
      type: Array,
      required: true
    }
  },
  methods: {
    onInputChange(value) {
      var router = this.$router
      router.push({
        name: 'search',
        params: {movieName:value}
      })
    },
  },
}
</script>