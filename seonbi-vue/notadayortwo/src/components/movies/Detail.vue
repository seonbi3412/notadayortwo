<template>
  <div class="detail">
    <h1>{{ movie.title }}</h1>
    <img :src="poster_url" :alt="movie.title">
    <h5>{{ movie.score }} | {{ movie.open_date }}</h5>
    <h5>장르: <span v-for="genre in movie.genres" :key="genre.id">{{ genre.name }} </span></h5>
    <p>{{ like_count }}</p>
    <button @click="likeMovie" v-if="!isLiked">좋아요</button>
    <button @click="likeMovie" v-else>좋아요 취소</button>
    <p>{{ movie.description }}</p>    
  </div>
</template>

<script>
import axios from 'axios'
import { mapGetters } from 'vuex'

export default {
  name: "detail",
  data() {
    return {
      movie: {},
      poster_url: "",
      isLiked: false,
      like_count: 0,
    }
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
          this.poster_url=`https://image.tmdb.org/t/p/w500${this.movie.poster_url}`
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
        this.poster_url=`https://image.tmdb.org/t/p/w500${this.movie.poster_url}`
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
}
</script>

<style>

</style>