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
      <b-container fluid class="p-2 bg-dark">
        <b-row>
          <b-col cols="2" v-for="actor in movie.actors" :key="actor.id">
            <b-img thumbnail fluid v-if="actor.profile_path" :src="`https://image.tmdb.org/t/p/w500${actor.profile_path}`" :alt="actor.name"></b-img>
          </b-col>
        </b-row>
      </b-container>
    </div>
    <div class="col-4 border border-dark rounded">
      <div class="reviewChat py-2">
        <div v-for="review in currentReviews" :key="review.id">
          <div v-if="review.movie === movie.id || review.movie_id === movie.id" class="border border-secondary rounded my-1">
            <p class="mb-0 d-inline">{{ review.content }} - {{ review.user.username }} | </p>
            <star-rating :star-size="10" :inline="true" :read-only="true" v-model="review.score"></star-rating>
          </div>
        </div>
      </div>
      <form @submit.prevent="createReview">
        <star-rating v-model="rating" :border-width="3" :star-size="10" :inline="true"></star-rating>
        <b-form-input type="text" v-model="content"></b-form-input>
        <button class="btn btn-info btn-sm" type="submit">등록</button>
      </form>
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
      currentReviews: [],
      movie: {},
      poster_url: "",
      isLiked: false,
      like_count: 0,
      videos: [],
      content: '',
      rating: 0,
    }
  },
  props: {
    users: {
      type: Array,
      required: true
    },
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
    createReview() {
      const data = {
        'content': this.content,
        'movie': this.movie.id,
        'user': this.user.user_id,
        'score': this.rating
      }
      axios.post(`http://127.0.0.1:8000/movies/reviews/`, data, this.options)
        .then(response => {
          let tmp_review = response.data
          this.users.forEach(user => {
            if (user.id === tmp_review.user) {
              tmp_review.user = user
            }
          })
          this.currentReviews.push(tmp_review)
          console.log(tmp_review)
          this.content = ''
          this.rating = 0
        })
        .catch(error => {
          console.log(error)
        })
    },
    likeMovie() {
      axios.post(`http://127.0.0.1:8000/movies/${this.movie.id}/like/`, this.user, this.options)
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
          this.$emit('redataload', true)
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  mounted() {
    axios.get(`http://127.0.0.1:8000/movies/${this.$route.params.id}/reviews/`)
      .then(response => {
        console.log('======================== ')
        console.log(response)
        this.currentReviews = response.data
        this.currentReviews.forEach(review => {
          this.users.forEach(user => {
            if (review.user === user.id) {
              review.user = user
            }
          })
        })
      })
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
div.reviewChat {
  height: 80vh;
  border-radius: 15px;
  overflow-y: scroll;
  -ms-overflow-style: none;
}
::-webkit-scrollbar {
  display:none;
} 
</style>