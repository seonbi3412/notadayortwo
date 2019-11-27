<template>
  <div class="movielistitem">
    <router-link :to="`/movies/${movie.id}`" :reviews="reviews" :users="users">
      <img :src="posterUrl" alt="">
    </router-link>
  </div>
</template>

<script>

export default {
  name: "movieListItem",
  data() {
    return {
      posterUrl: `https://image.tmdb.org/t/p/w300${this.movie.poster_url}`
    }
  },
  props: {
    movie: {
      type: Object,
      required: true
    },
    reviews: {
      type: Array,
      required: true
    },
    users: {
      type: Array,
      required: true
    }
  },
}
</script>

<style>
</style>