<template>
  <div class="search container">
    <search-bar class="" :movies="movies" :actors="actors" :genres="genres" @input-change-event="onInputChange"/>
    
    <h1 class="text-light">영화</h1>
    <div class="row">
      <div class="moviecard col-4" v-for="movie in searchMovies" :key="`movie-${movie.id}`">
        <div class="flip-card">
          <div class="flip-card-inner">
            <div class="flip-card-front">
              <MovieListItem class="" :movie="movie" :reviews="reviews"/>  
            </div>
            <div class="flip-card-back container d-flex flex-wrap flex-column py-5 justify-content-center align-items-center">
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
    <h1 class="text-light">배우</h1>
    <div class="row">
      <div class="col-4"  v-for="actor in searchActors" :key="actor.id">
        <div class="flip-card">
          <div class="flip-card-inner">
            <div class="flip-card-front">
              <ActorListItem class="" :actor="actor" :reviews="reviews"/>  
            </div>
            <div class="flip-card-back container d-flex flex-column py-5 justify-content-center align-items-center">
              <h1 class="text-info">{{ actor.name }}</h1>
              <br>
              <div>
                {{ actor.birthday }}
              </div>
              <br>
              <div>
                <p>필모그래피</p>
                <p class="mb-0" v-for="filmo in actor.filmography" :key="filmo.id">
                  {{ filmo.title }}
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar.vue'
import MovieListItem from '@/components/movies/MovieListItem.vue'
import ActorListItem from '@/components/actors/ActorListItem.vue'

export default {
  name: "search",
  components:{
    SearchBar,
    MovieListItem,
    ActorListItem,
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
      searchMovies: {},
      searchActors: {}
    }
  },
  methods: {
    onInputChange(value) {
      this.searchMovies = this.movies.filter(movie => {
        if(movie.title.includes(value)){
          return movie
        }
        let selectMovie = movie.genres.filter(genre => {
          if(genre.name.includes(value)){
            return genre
            }
        })
        if (selectMovie.length > 0){
          return selectMovie
        }
      })
      this.searchActors = this.actors.filter(actor => actor.name.includes(value))
    },
  },
  mounted() {
    if (this.$route.params.movieName){
      this.searchMovies = this.movies.filter(movie => {
        if(movie.title.includes(this.$route.params.movieName)){
          return movie
        }
        let selectMovie = movie.genres.filter(genre => {
          if(genre.name.includes(this.$route.params.movieName)){
            return genre
            }
        })
        if (selectMovie.length > 0){
          return selectMovie
        }
      })
      this.searchActors = this.actors.filter(actor => actor.name.includes(this.$route.params.movieName))
    }
    else{
      this.searchMovies = this.movies
      this.searchActors = this.actors
    }
  }
}
</script>

<style>
.flip-card {
  background-color: transparent;
  width: 300px;
  height: 450px;
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
  color: black;
}

/* Style the back side */
.flip-card-back {
  background-color: #333333;
  color: white;
  transform: rotateY(180deg);
}

</style>