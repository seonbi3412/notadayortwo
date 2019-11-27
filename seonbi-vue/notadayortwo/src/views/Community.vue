<template>
  <div class="community">
    <router-view ></router-view>
    <all :reviews="reviews" :users="users" :movies="movies"/>
    <!-- <select class="form-control" v-model="selectedGenreId">
      <option v-for="movie in movies" :key="movie.id" :value="movie.id">{{movie.name}}</option>
    </select> -->
    <!-- <selected :reviews="selectedReviews"/> -->
  </div>
</template>

<script>
// @ is an alias to /src
import All from '@/components/community/All.vue'
// import Selected from '@/components/community/Selected.vue'
// import { mapGetters } from 'vuex'

export default {
  name: 'community',
  components: {
    All,
    // Selected
  },
  props: {
    movies: {
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
  data() {
    return {
    }
  },
  computed: {
    // selectedReview() {
    //   if (this.selecte === ''){
    //     return {}
    //   }
    //   return this.reviews.filter(review => review.movie_id === this.selecte)
    // },
    // ...mapGetters([
    //   'options',
    //   'user'
    // ])
  },
}
</script>