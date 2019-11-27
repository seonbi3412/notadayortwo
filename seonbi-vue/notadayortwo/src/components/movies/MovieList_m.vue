<template>
  <div class="movielist_m ">
    <div>
      <b-button
      :class="visible ? null : 'collapsed'"
      :aria-expanded="visible ? 'true' : 'false'"
      v-b-toggle.collapse-genre.collapse-country
      @click="test"
    >
      필터 선택
    </b-button>
    <b-collapse id="collaps-genre" v-model="visible" class="mt-2">
      <b-form-group label="장르">
        <b-form-checkbox-group
          v-model="selectedGenres"
          :options="filterGenres"
          name="buttons-1"
          buttons
        ></b-form-checkbox-group>
      </b-form-group>
    </b-collapse>
    <b-collapse id="collaps-country" v-model="visible" class="mt-2">
      <b-form-group label="국가">
        <b-form-checkbox-group
          v-model="selectedCountry"
          :options="filterCountry"
          name="buttons-2"
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
      selectedGenres: [], // Must be an array reference!
      selectedCountry: [],
      filterGenres: [],
      filterCountry: [{text: "에스토니아",value: "에스토니아"},
                      {text: "튀니지",value: "튀니지"},
                      {text: "프랑스",value: "프랑스"},
                      {text: "미국",value: "미국"},
                      {text: "독일",value: "독일"},
                      {text: "대만",value: "대만"},
                      {text: "아르헨티나",value: "아르헨티나"},
                      {text: "영국",value: "영국"},
                      {text: "슬로바키아",value: "슬로바키아"},
                      {text: "인도",value: "인도"},
                      {text: "중국",value: "중국"},
                      {text: "브라질",value: "브라질"},
                      {text: "브루나이",value: "브루나이"},
                      {text: "폴란드",value: "폴란드"},
                      {text: "캐나다",value: "캐나다"},
                      {text: "이탈리아",value: "이탈리아"},
                      {text: "베트남",value: "베트남"},
                      {text: "호주",value: "호주"},
                      {text: "스웨덴",value: "스웨덴"},
                      {text: "덴마크",value: "덴마크"},
                      {text: "나이지리아",value: "나이지리아"},
                      {text: "벨기에",value: "벨기에"},
                      {text: "태국",value: "태국"},
                      {text: "일본",value: "일본"},
                      {text: "러시아",value: "러시아"},
                      {text: "싱가포르",value: "싱가포르"},
                      {text: "캄보디아",value: "캄보디아"},
                      {text: "한국",value: "한국"}],
      visible: false
    }
  },
  computed: {
    movies_genre() {
      if (this.selectedGenres.length === 0 && this.selectedCountry.length===0){ // 초기값일땐 모든 영화 출력
        return this.movies
      }
      return this.movies.filter(movie => {
        if(this.selectedCountry.includes(movie.country)){
          return movie
        }
        let selectMovie = movie.genres.filter(genre => {
          if(this.selectedGenres.includes(genre.id)){
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
      if(this.filterGenres.length===0){
        let temp = []
        let pregenres = this.$props.genres
        for(let idx in pregenres){
          temp.push({text: pregenres[idx]["name"], value: pregenres[idx]["id"]})
        }
        this.filterGenres = temp
      }
    }
  },
}
</script>

<style>

</style>
