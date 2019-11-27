<template>
  <div class="movielist_m ">
    <div>
      <b-button
      :class="visible ? null : 'collapsed'"
      :aria-expanded="visible ? 'true' : 'false'"
      aria-controls="collapse-4"
      @click="test"
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
      selected: [], // Must be an array reference!
      filteroptions: [],
      visible: false
    }
  },
  computed: {
    movies_genre() {
      if (this.selected.length === 0){ // 초기값일땐 모든 영화 출력
        return this.movies
      }
      return this.movies.filter(movie => {
        let selectMovie = movie.genres.filter(genre => {
          if(this.selected.includes(genre.id)){
            return genre
            }
        })
        if (selectMovie.length > 0){
          return selectMovie
        }
      })
    }
  },
  methods: {
    test() {
      this.visible = !this.visible
      if(this.filteroptions.length===0){
        let temp = []
        let pregenres = this.$props.genres
        for(let idx in pregenres){
          temp.push({text: pregenres[idx]["name"], value: pregenres[idx]["id"]})
        }
        this.filteroptions = temp
      }
    }
  },
}
</script>

<style>

</style>
