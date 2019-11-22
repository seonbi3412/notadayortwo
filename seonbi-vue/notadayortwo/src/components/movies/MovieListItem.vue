<template>
  <div class="movielistitem">
    <p>{{ movie.title }}</p>
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
  }
}
</script>

<style>

</style>