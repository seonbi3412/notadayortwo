<template>
  <div class="community">
    <div id="nav">
      <router-link to="/" exact>Home</router-link> |
      <router-link to="/movies">Movies</router-link> |
      <router-link to="/account">Account</router-link> |
      <router-link to="/account/login">Login</router-link> |
      <router-link to="/account/signup">Signup</router-link> |
      <router-link to="/community">Community</router-link>
    </div>
    <router-view ></router-view>
    <h1>This is a community page</h1>
    <all :reviews="reviews"/>
    <select class="form-control" v-model="selectedGenreId">
    // 선택된 장르의 아이디를 selectedGenreId에 바인딩
      <option v-for="movie in movies" :key="movie.id" :value="movie.id">{{movie.name}}</option>
    </select>
    <selected :reviews="selectedReviews"/>
  </div>
</template>

<script>
// @ is an alias to /src
import All from '@/components/community/All.vue'
import Selected from '@/components/community/Selected.vue'
import axios from 'axios'

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
    }
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
    axios.get(`http://127.0.0.1:8000/review`)
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