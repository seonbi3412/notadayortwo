<template>
  <div class="movie-list">
    <h2>영화목록</h2>
    <ul>
      <li
        v-for="movie in movies"
        :key="movie.id"
      >
      {{ movie.title }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'MovieList',
  props: {
    movies: {
      type: Array,
      required: true
    }
  },
  methods: {
  
  }
}
</script>

<style>
</style>