<template>
  <div class="home">
    <search-bar class="my-3" :movies="movies" @input-change-event="onInputChange"/>
    <!-- <movie-list :movies="movies"/> -->

    <Swiper class="my-5" :movies="movies"/>
  </div>
</template>

<script>
// @ is an alias to /src
import SearchBar from '@/components/SearchBar.vue'
// import MovieList from '@/components/home/MovieList_h.vue'
import Swiper from '@/components/Swiper.vue'

export default {
  name: 'home',
  components: {
    SearchBar,
    // MovieList,
    Swiper
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

<style>
</style>