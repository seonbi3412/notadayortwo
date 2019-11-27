<template>
  <div class="detail container d-flex justify-content-center align-items-center">
    <div class="col-4">
      <h1>{{ movie.title }}</h1>
      <img :src="poster_url" :alt="movie.title">
    </div>
    <div class="col-8 d-flex flex-column">
      <videos class="col-12" :videos="videos"/>
      <h5>{{ movie.score }} | {{ movie.open_date }}</h5>
      <h5>장르: <span v-for="genre in movie.genres" :key="genre.id">{{ genre.name }} </span></h5>
      <p>{{ like_count }}</p>
      <div class="container">
        <button class="btn btn-secondary" @click="likeMovie" v-if="!isLiked && this.user">좋아요</button>
        <button class="btn btn-secondary" @click="likeMovie" v-else-if="this.user">좋아요 취소</button>
      </div>
      <div class="container">
        <p>{{ movie.description }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapGetters } from 'vuex'
import Videos from './Videos.vue'
export default {
  name: "detail",
  data() {
    return {
      movie: {},
      poster_url: "",
      isLiked: false,
      like_count: 0,
      videos: []
    }
  },
  components: {
    Videos
  },
  computed: {
    ...mapGetters([
      'options',
      'user'
    ]),
  },
  methods: {
    likeMovie() {
      axios.post(`http://127.0.0.1:8000/movies/${this.movie.id}/like/`, this.user)
        .then(response => {
          this.movie = response.data
          this.like_count = this.movie.like_users.length
          this.poster_url=`https://image.tmdb.org/t/p/w300${this.movie.poster_url}`
          this.isLiked = false
          for(let idx in this.movie.like_users){
            if (this.movie.like_users[idx].id === this.user.user_id){
              this.isLiked = true
              break
            }
          }
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  mounted() {
    axios.get(`http://127.0.0.1:8000/movies/${this.$route.params.id}/`)
      .then(response => {
        this.movie = response.data
        this.like_count = this.movie.like_users.length
        this.poster_url=`https://image.tmdb.org/t/p/w300${this.movie.poster_url}`
        this.isLiked = false
          for(let idx in this.movie.like_users){
            if (this.movie.like_users[idx].id === this.user.user_id){
              this.isLiked = true
              break
            }
          }
        return this.movie
      })
      .then(movie => {
        axios.get(`https://api.themoviedb.org/3/movie/${movie.id}/videos?api_key=6b356c5ae179a5d932c01687a436b72e&language=ko-KR`)
          .then(response => {
            console.log(response.data.results)
            this.videos = response.data.results
          })
          .catch(error => {
            console.log(error)
          })
      })
      .catch(error => {
        console.log(error)
      })
  }
}
</script>

<style>
div.detail {
  width: 3000px;
  height: 100vh;
}
</style>