<template>
  <div class="home">
    <search-bar @input-change-event="onInputChange"/>
    <movie-list :movies="movies"/>
  </div>
</template>

<script>
// @ is an alias to /src
import SearchBar from '@/components/SearchBar.vue'
import MovieList from '@/components/MovieList.vue'

export default {
  name: 'home',
  components: {
    SearchBar,
    MovieList
  },
  data() {
    return {
      movies: [],
    }
  },
  methods: {
    onInputChange(value) {
      console.log('searchbar -> home')
      console.log(value)
    },
  },
  mounted() {
    this.movies =[{title:'조커', id:1}, {title:'말레피센트', id:2}]
  },
}
</script>
