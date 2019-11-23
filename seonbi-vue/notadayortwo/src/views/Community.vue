<template>
  <div class="community">
    <div id="nav">
      <router-link to="/" exact>Home</router-link> |
      <router-link to="/movies">Movies</router-link> |
      <router-link to="/account">Account</router-link> |
       <div v-if="!isAuthenticated">
        <router-link to="/account/login">Login</router-link> |
        <router-link to="/account/signup">Signup</router-link> |
      </div>
      <div v-else>
        <a @click.prevent="logout" href="#">Logout</a>
      </div>
      <router-link to="/community">Community</router-link>
    </div>
    <router-view ></router-view>
    <h1>This is a community page</h1>
    <all :reviews="reviews"/>
    <!-- <select class="form-control" v-model="selectedGenreId">
      <option v-for="movie in movies" :key="movie.id" :value="movie.id">{{movie.name}}</option>
    </select> -->
    <selected :reviews="selectedReviews"/>
  </div>
</template>

<script>
// @ is an alias to /src
import All from '@/components/community/All.vue'
import Selected from '@/components/community/Selected.vue'
import axios from 'axios'
import router from '../router'

export default {
  name: 'community',
  components: {
    All,
    Selected
  },
  data() {
    return {
      reviews: {},
      selecte: '',
      isAuthenticated: this.$session.has('jwt')
    }
  },
   methods: {
     isLogin() {
      this.$session.start()
      if (this.$session.has('jwt')) {
        this.$store.dispatch('login', this.$session.get('jwt'))
      }
    },
    logout() {
      this.$session.destroy()
      this.$store.dispatch('logout')
      router.push('/')
    }
  },
  updated() {
    this.isAuthenticated = this.$session.has('jwt')
  },
  computed: {
    selectedReview() {
      if (this.selecte === ''){
        return {}
      }
      return this.reviews.filter(review => review.movie_id === this.selecte)
    }
  },
  mounted() {
    this.isLogin()
    axios.get(`http://127.0.0.1:8000/movies/reviews/`)
    .then(response =>{
      console.log(response.data)
      this.reviews = response.data
    })
    .catch(error => {
      console.log(error)
    })
  },
}
</script>