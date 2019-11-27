<template>
  <div class="search container">
    <search-bar class="" :movies="movies" :actors="actors" :genres="genres" @input-change-event="onInputChange"/>
    
    <h1>영화</h1>
    <div class="row">
      <div class="col-4" v-for="movie in searchMovies" :key="`movie-${movie.id}`">
        <div class="flip-card">
          <div class="flip-card-inner">
            <div class="flip-card-front">
              <MovieListItem class="" :movie="movie" :reviews="reviews"/>  
            </div>
            <div class="flip-card-back container d-flex flex-column py-5">
              <h1>{{ movie.title }}</h1>
              <div>
                <button 
                  class="btn btn-sm btn-info m-1" 
                  :class="{ 'btn-danger': genre.id === 28,'btn-warning': genre.id === 16, 'btn-info': genre.id === 14 }" 
                  v-for="genre in movie.genres" :key="genre.id">{{ genre.name }}</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>


    
    <h1>배우</h1>
    <div class="row">
      <ActorListItem class="" v-for="actor in searchActors" :key="actor.id" :actor="actor" :reviews="reviews"/>
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
  border: 1px solid #f1f1f1;
  perspective: 1000px; /* Remove this if you don't want the 3D effect */
}

/* This container is needed to position the front and back side */
.flip-card-inner {
  position: relative;
  width: 100%;
  height: 100%;
  text-align: center;
  transition: transform 0.8s;
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
  background-color: dodgerblue;
  color: white;
  transform: rotateY(180deg);
  overflow: scroll;
}
</style>