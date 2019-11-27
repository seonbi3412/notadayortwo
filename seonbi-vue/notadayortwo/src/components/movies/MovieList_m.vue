<template>
  <div class="movielist_m">
    <div class="container">
      <div class="row">
        <div class="col-12 text-light">
          <b-button
          :class="visible ? null : 'collapsed'"
          :aria-expanded="visible ? 'true' : 'false'"
          v-b-toggle.collapse-genre.collapse-continent
          @click="test"
          >필터 선택</b-button>
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
          <b-collapse id="collaps-continent" v-model="visible" class="mt-2">
            <div class="d-flex justify-content-around">
              <div>
                <b-button class="slow" v-b-toggle.collapse-asia size="sm">asia</b-button>
                <b-collapse id="collapse-asia" class="mt-2">
                  <b-form-group>
                    <b-form-checkbox-group
                      v-model="selectedCountry"
                      :options="filterAsia"
                      name="buttons-2"
                      buttons
                    ></b-form-checkbox-group>
                  </b-form-group>
                </b-collapse>
              </div>
              <div>
                <b-button class="slow" v-b-toggle.collapse-europe size="sm">europe</b-button>
                <b-collapse id="collapse-europe" class="mt-2">
                  <b-form-group>
                    <b-form-checkbox-group
                      v-model="selectedCountry"
                      :options="filterEurope"
                      name="buttons-2"
                      buttons
                    ></b-form-checkbox-group>
                  </b-form-group>
                </b-collapse>
              </div>
              <div>
                <b-button class="slow" v-b-toggle.collapse-america size="sm">america</b-button>
                <b-collapse id="collapse-america" class="mt-2">
                  <b-form-group>
                    <b-form-checkbox-group
                      v-model="selectedCountry"
                      :options="filterAmerica"
                      stacked
                      name="buttons-2"
                      buttons
                    ></b-form-checkbox-group>
                  </b-form-group>
                </b-collapse>
              </div>
              <div>
                <b-button class="slow" v-b-toggle.collapse-africa size="sm">africa</b-button>
                <b-collapse id="collapse-africa" class="mt-2">
                  <b-form-group>
                    <b-form-checkbox-group
                      v-model="selectedCountry"
                      :options="filterAfrica"
                      name="buttons-2"
                      buttons
                    ></b-form-checkbox-group>
                  </b-form-group>
                </b-collapse>
              </div>
              <div>
                <b-button class="slow" v-b-toggle.collapse-oceania size="sm">oceania</b-button>
                <b-collapse id="collapse-oceania" class="mt-2">
                  <b-form-group>
                    <b-form-checkbox-group
                      v-model="selectedCountry"
                      :options="filterOceania"
                      name="buttons-2"
                      buttons
                    ></b-form-checkbox-group>
                  </b-form-group>
                </b-collapse>
              </div>
            </div>
          </b-collapse>
        </div>
      </div>
    </div>
    <br>
    <div class="d-flex flex-wrap justify-content-center">
      <div class="" v-for="movie in movies_genre" :key="`movie-${movie.id}`">
        <div class="flip-card">
          <div class="flip-card-inner">
            <div class="flip-card-front">
              <MovieListItem class="" :movie="movie" :reviews="reviews" :users="users"/>  
            </div>
            <div class="flip-card-back container d-flex flex-column justify-content-center align-items-center py-5">
              <h1>{{ movie.title }}</h1>
              <div>
                <button
                  class="btn btn-sm m-1 text-light" 
                  :class="{ 'btn-danger': genre.id === 28 || genre.id === 80 || genre.id === 53 || genre.id === 10752,
                            'btn-warning': genre.id === 16 || genre.id === 35 || genre.id === 18 || genre.id === 10751 || genre.id === 10749,
                            'btn-info': genre.id === 14 || genre.id === 878 || genre.id === 12, 
                            'btn-success': genre.id === 99 || genre.id === 36 || genre.id === 10402 || genre.id === 10770 || genre.id === 37,
                            'btn-primary': genre.id === 9648 || genre.id === 27 }"
                  v-for="genre in movie.genres" :key="genre.id">{{ genre.name }}</button>
              </div>
              <div class="my-3">
                <star-rating v-model="movie.score" read-only="true" star-size="40"></star-rating>
              </div>
            </div>
          </div>
        </div>
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
      filterAsia: [{text: "한국",value: "한국"},
                   {text: "대만",value: "대만"},
                   {text: "인도",value: "인도"},
                   {text: "중국",value: "중국"},
                   {text: "브루나이",value: "브루나이"},
                   {text: "베트남",value: "베트남"},
                   {text: "태국",value: "태국"},
                   {text: "일본",value: "일본"},
                   {text: "러시아",value: "러시아"},
                   {text: "싱가포르",value: "싱가포르"},
                   {text: "캄보디아",value: "캄보디아"}],
      filterAfrica: [{text: "튀니지",value: "튀니지"},
                     {text: "나이지리아",value: "나이지리아"}],
      filterAmerica: [{text: "미국",value: "미국"},
                      {text: "캐나다",value: "캐나다"},
                      {text: "아르헨티나",value: "아르헨티나"},
                      {text: "브라질",value: "브라질"}],
      filterEurope:[{text: "에스토니아",value: "에스토니아"},
                    {text: "프랑스",value: "프랑스"},
                    {text: "독일",value: "독일"},
                    {text: "영국",value: "영국"},
                    {text: "슬로바키아",value: "슬로바키아"},
                    {text: "폴란드",value: "폴란드"},
                    {text: "이탈리아",value: "이탈리아"},
                    {text: "스웨덴",value: "스웨덴"},
                    {text: "덴마크",value: "덴마크"},
                    {text: "벨기에",value: "벨기에"}],
      filterOceania: [{text: "호주",value: "호주"}],
      visible: false
    }
  },
  computed: {
    movies_genre() {
      if(this.selectedGenres.length > 0 && this.selectedCountry.length > 0){
        return this.movies.filter(movie => {
              if(this.selectedCountry.includes(movie.country)){
                let selectMovie = movie.genres.filter(genre => {
                  if(this.selectedGenres.includes(genre.id)){
                    return genre
                  }
                })
                if (selectMovie.length > 0){
                  return selectMovie
                }
              }
            })
      }
      else if(this.selectedGenres.length === 0 && this.selectedCountry.length > 0){
        return this.movies.filter(movie => { 
          if(this.selectedCountry.includes(movie.country)){
            return movie
          } 
        })
      }
      else if (this.selectedGenres.length > 0 && this.selectedCountry.length===0){ 
        return this.movies.filter(movie => {
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
      else{return this.movies}
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
.flip-card {
  background-color: transparent;
  width: 300px;
  height: 430px;
  perspective: 1000px; /* Remove this if you don't want the 3D effect */
}

/* This container is needed to position the front and back side */
.flip-card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  text-align: center;
  transition: transform 1s;
  transform-style: preserve-3d;
}

/* Do an horizontal flip when you move the mouse over the flip box container */
.flip-card:hover .flip-card-inner {
  transform: rotateY(180deg);
}

/* Position the front and back side */
.flip-card-front, .flip-card-back {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
}

/* Style the front side (fallback if image is missing) */
.flip-card-front {
  background-color: #bbb;
  color: black;
}

/* Style the back side */
.flip-card-back {
  background-color: #333333;
  color: white;
  transform: rotateY(180deg);
}

</style>