<template>
  <div class="detail">
    <h1>{{ movie.title }}</h1>
    <img :src="poster_url" :alt="movie.title">
    <h5>{{ movie.score }} | {{ movie.open_date }}</h5>
    <h5>장르: <span v-for="genre in movie.genres" :key="genre.id">{{ genre.name }} </span></h5>
    <p>{{ this.likeUsers }}</p>
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
      movieDetail: {},
      poster_url: `https://image.tmdb.org/t/p/w500${this.movie.poster_url}`,
      isLiked: false,
      likeUsers: 0,
    }
  },
  props: {
    movie: {
      type: Object,
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
      console.log(this.user)
      console.log('좋아요!!!')
      axios.post(`http://127.0.0.1:8000/movies/${this.movie.id}/like/`, this.user)
        .then(response => {
          console.log(response)
          this.$set(this.$data, 'likeUsers', response.data.like_count)
          this.$set(this.$data, 'isLiked', response.data.is_liked)
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  // created() {
    // searchLikeUsers() {
      // axios.get(`http://127.0.0.1:8000/movies/${this.$route.params.id}/like/`, this.user)
      //   .then(response => {
      //     console.log(response)
      //     this.$set(this.$data, 'likeUsers', response.data.like_count)
      //     this.$set(this.$data, 'isLiked', response.data.is_liked)
      //     console.log(this.isLiked)
      //   })
      //   .catch(error => {
      //     console.log(error)
      //   })
    // }
  // },
  beforeMount() {
    if (this.movie) {
      this.movieDetail = this.movie
      console.log('props로!!!')
    } else {
      axios.get(`http://127.0.0.1:8000/movies/${this.$route.params.id}/`)
          .then(response => {
            console.log(response)
            this.movieDetail = response.data
            console.log('axios로!!!')
          })
    }
    console.log(this.movie)
  }
}
</script>

<style>

</style>