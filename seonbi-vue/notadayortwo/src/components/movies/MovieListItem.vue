<template>
  <div class="movielistitem">
    <router-link :to="{ name: 'detail', params: {'movie': movie} }">
      <img :src="posterUrl" alt="">
      <p>{{ movie.title }}</p>
    </router-link>
  </div>
</template>

<script>

export default {
  name: "movieListItem",
  data() {
    return {
      posterUrl: `https://image.tmdb.org/t/p/w400${this.movie.poster_url}`
    }
  },
  props: {
    movie: {
      type: Object,
      required: true
    }
  },
}
</script>

<style>
</style>