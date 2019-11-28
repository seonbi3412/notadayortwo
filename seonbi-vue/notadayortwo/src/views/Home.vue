<template>
  <div class="home d-flex justify-content-center row">
    <!-- <search-bar class="my-3" :movies="movies" @input-change-event="onInputChange"/> -->
    <!-- <movie-list :movies="movies"/> -->
    <Boxoffice class="my-5 col-8" :boxoffice="boxoffice" :reviews="reviews"/>  
    <RecommendMovies class="my-5 col-4" :movies="movies" :reviews="reviews" :users="users"/>
  </div>
</template>

<script>
// @ is an alias to /src
// import SearchBar from '@/components/SearchBar.vue'
// import MovieList from '@/components/home/MovieList_h.vue'
import Boxoffice from '@/components/home/Boxoffice.vue'
import RecommendMovies from '@/components/home/RecommendMovies.vue'
import axios from 'axios'
import { mapGetters } from 'vuex'

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
    reMovies: {
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
  methods: {
    onInputChange(value) {
      var router = this.$router
      router.push({
        name: 'search',
        params: {movieName:value}
      })
    },
  },
  computed: {
    ...mapGetters([
      'options',
      'user'
    ])
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
  div {
    background-color: rgba(0, 0, 0, 0);
  }
</style>