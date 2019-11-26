<template>
  <div class="home">
    <!-- <search-bar class="my-3" :movies="movies" @input-change-event="onInputChange"/> -->
    <!-- <movie-list :movies="movies"/> -->
    <Boxoffice class="my-5" :boxoffice="boxoffice"/>
    <RecommendMovies class="my-5" :movies="movies"/>
  </div>
</template>

<script>
// @ is an alias to /src
// import SearchBar from '@/components/SearchBar.vue'
// import MovieList from '@/components/home/MovieList_h.vue'
import Boxoffice from '@/components/Boxoffice.vue'
import RecommendMovies from '@/components/RecommendMovies.vue'
import axios from 'axios'

export default {
  name: 'home',
  components: {
    // SearchBar,
    // MovieList,
    Boxoffice,
    RecommendMovies
  },
  data() {
    return {
      boxoffice: [],
    }
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
  methods: {
    onInputChange(value) {
      var router = this.$router
      router.push({
        name: 'search',
        params: {movieName:value}
      })
    },
  },
  mounted() {
    axios.get('http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=20ea3580299a37f479eee8e01bc91ded&targetDt=20191125&itemPerPage=10')
      .then(response => {
        console.log(response.data.boxOfficeResult.dailyBoxOfficeList)
        this.boxoffice = response.data.boxOfficeResult.dailyBoxOfficeList
        this.boxoffice = this.boxoffice.map(box => {
          let mov = this.movies.filter(movie => {
            return box.movieNm === movie.title
          })
          return {...box, poster_url: mov.length > 0 ? mov[0].poster_url : ''}
        })
        console.log(this.boxoffice)
      })
      .catch(error => {
        console.log(error)
      })
  }
}
</script>

<style>
</style>