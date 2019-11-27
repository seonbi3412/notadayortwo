<template>
  <div class="movielist_m ">
    <div>
      <b-button
      :class="visible ? null : 'collapsed'"
      :aria-expanded="visible ? 'true' : 'false'"
      aria-controls="collapse-4"
      @click="visible = !visible"
    >
      필터 선택
    </b-button>
    <b-collapse id="collapse-4" v-model="visible" class="mt-2">
      <b-form-group label="장르">
        <b-form-checkbox-group
          v-model="selected"
          :options="filteroptions"
          name="buttons-1"
          buttons
        ></b-form-checkbox-group>
      </b-form-group>
    </b-collapse>
    </div>


    <select class="form-control mx-auto row" style="width: 400px;" v-model="selectedGenreId">
      <option value="0">장르 선택</option>
      <option v-for="genre in genres" :key="genre.id" :value="genre.id">{{genre.name}}</option>
    </select>
    <div class="container d-flex justify-content-center my-4">
      <div class="row">
        <MovieListItem class="col-12 col-md-6 col-xl-4" v-for="movie in movies_genre" :key="movie.id" :movie="movie" :reviews="reviews" :users="users"/>
      </div>
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
    reviews: {
      type: Array,
      required: true
    }
  },
  data () {
    return {
      selectedGenreId: "0", // 데이터 초기화,
      selected: [], // Must be an array reference!
      filteroptions: [],
      visible: true
    }
  },
  computed: {
    movies_genre() {
      if (this.selectedGenreId === "0"){ // 초기값일땐 모든 영화 출력
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
  mounted() {
    let temp = []
    console.log(this.$props.genres)
    let pregenres = this.$props.genres
    for(let idx in pregenres){
      temp.push({text: pregenres[idx]["name"], value: pregenres[idx]["id"]})
    }
    this.filteroptions = temp
  },
}
</script>

<style>

</style>
