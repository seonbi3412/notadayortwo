<template>
  <div class="community">
    <router-view ></router-view>
    <h1>This is a community page</h1>
    <all :reviews="reviews"/>
    <!-- <select class="form-control" v-model="selectedGenreId">
      <option v-for="movie in movies" :key="movie.id" :value="movie.id">{{movie.name}}</option>
    </select> -->
    <selected :reviews="selectedReview"/>
  </div>
</template>

<script>
// @ is an alias to /src
import All from '@/components/community/All.vue'
import Selected from '@/components/community/Selected.vue'
import { mapGetters } from 'vuex'
import axios from 'axios'

export default {
  name: 'community',
  components: {
    All,
    Selected
  },
  data() {
    return {
      reviews: [],
      selecte: '',
    }
  },
  computed: {
    myreviews() {
      return this.reviews.map(review => {
        return {...review, isUpdate: false}
      })
    },
    selectedReview() {
      if (this.selecte === ''){
        return {}
      }
      return this.reviews.filter(review => review.movie_id === this.selecte)
    },
    ...mapGetters([
      'options',
      'user'
    ])
  },
  mounted() {
    axios.get(`http://127.0.0.1:8000/movies/reviews/`)
    .then(response =>{
      this.reviews = response.data.map(data => {
        return {...data, updated: false}
      })
    })
    .catch(error => {
      console.log(error)
    })
  },
}
</script>