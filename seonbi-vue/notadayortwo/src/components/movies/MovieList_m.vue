<template>
  <div class="movielist_m ">
    <select class="form-control mx-auto row" style="width: 400px;" v-model="selectedGenreId">
      <option v-for="genre in genres" :key="genre.id" :value="genre.id">{{genre.name}}</option>
    </select>
    <div class="container row my-4">
      <MovieListItem class="col-12 col-md-6 col-xl-4" v-for="movie in movies_genre" :key="movie.id" :movie="movie"/>
    </div>
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
  },
  data () {
    return {
      selectedGenreId: 0, // 데이터 초기화
    }
  },
  computed: {
    movies_genre() {
      if (this.selectedGenreId === 0){ // 초기값일땐 모든 영화 출력
        return this.movies
      }
      return this.movies.filter(movie => {
        let selectMovie = movie.genres.filter(genre => {
          if(genre.id === this.selectedGenreId){
            return genre
            }
        })
        if (selectMovie.length > 0){
          return selectMovie
        }
      })
    }
  },
}
</script>

<style>

</style>
