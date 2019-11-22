<template>
  <div class="movielistitem">
    <router-link :to="{ name: 'detail', params: {'movie': movie} }">{{ movie.title }}</router-link>
  </div>
</template>

<script>

export default {
  name: "movieListItem",
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