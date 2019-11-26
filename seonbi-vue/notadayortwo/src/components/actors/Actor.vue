<template>
  <div class="actor">
    
  </div>
</template>

<script>
import axios from 'axios'
import { mapGetters } from 'vuex'
export default {
  name: "actor",
data() {
    return {
      actor: {},
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