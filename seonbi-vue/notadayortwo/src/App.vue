<template>
  <div id="app" class="text-dark">
    <div v-if="!this.$route.path.includes('/account/login') && !this.$route.path.includes('/account/signup')">
      <Nav :genres="genres" :movies="movies" :users="users" :actors="actors" :reviews="reviews" @redataload="loadDBdata"/>
    </div>
    <router-view :genres="genres" :movies="movies" :users="users" :actors="actors" :reviews="reviews" :reMovies="reMovies" @redataload="loadDBdata"/>
    <font-awesome-icon icon="user-secret" />
  </div>
</template>

<script>
// @ is an alias to /src
import Nav from './views/Nav.vue'
import { mapGetters } from 'vuex'
import axios from 'axios'

export default {
  name: 'app',
  components: {
    Nav
  },
  data() {
    return {
      movies: [],
      genres: [],
      users: [],
      actors: [],
      reviews: [],
      reMovies: [],
    }
  },
  computed: {
    ...mapGetters([
      'options',
      'user'
    ])
  },
  methods: {
    isLogin() {
      this.$session.start()
      if (this.$session.has('jwt')) {
        this.$store.dispatch('login', this.$session.get('jwt'))
      }
    },
    loadDBdata() {
      axios.get(`http://127.0.0.1:8000/movies/`)
        .then(response =>{
          this.movies = response.data
        })
        .catch(error => {
          console.log(error)
        })

      axios.get(`http://127.0.0.1:8000/movies/genres/`)
        .then(response =>{
          this.genres = response.data
        })
        .catch(error => {
          console.log(error)
        })

      axios.get(`http://127.0.0.1:8000/movies/users/`)
        .then(response =>{
          this.users = response.data

          let data = {
            'user': -1
          }
          if(this.user.user_id > 0){
            // console.log(this.users)
            data = {
              'user': this.users[this.user.user_id-1]
            }
          }

          console.log(data)

          axios.post(`http://127.0.0.1:8000/movies/recommend/`, data)
            .then(response => {
              console.log(response)
            })
            .catch(error => {
              console.log(error)
            })

        })
        .catch(error => {
          console.log(error)
        }),
      axios.get(`http://127.0.0.1:8000/movies/actors/`)
        .then(response =>{
          this.actors = response.data
        })
        .catch(error => {
          console.log(error)
        })

      axios.get(`http://127.0.0.1:8000/movies/reviews/`)
        .then(response =>{
          this.reviews = response.data.map(data => {
            return {...data, updated: false}
          })
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  mounted() {
    this.loadDBdata()
  },
}
</script>

<style>
@import url(//fonts.googleapis.com/earlyaccess/hanna.css);
/* @import url(//db.onlinewebfonts.com/c/48e8fdcae584b7ce6ca765d7ddda0874?family=Komika+Boogie); */
@font-face { font-family: 'BMJUA'; src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_one@1.0/BMJUA.woff') format('woff'); font-weight: normal; font-style: normal; }

#app {
  font-family: 'Hanna', fantasy, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
body {
  background-image: url('./assets/bg.jpg');
  background-size: cover;
  background-repeat: no-repeat;
  background-attachment: fixed;  
}
</style>