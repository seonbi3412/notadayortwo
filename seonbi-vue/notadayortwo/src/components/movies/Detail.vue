<template>
  <div class="detail">
    <h1>This is a {{ movie.title}} page</h1>
    
    
  </div>
</template>

<script>

export default {
  name: "detail",
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