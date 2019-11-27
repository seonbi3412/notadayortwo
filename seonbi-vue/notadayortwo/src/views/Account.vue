<template>
  <div class="account">
    <router-view :genres="genres" :users="users"/>
  </div>
</template>
<script>
export default {
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
  },
}
</script>

<style>

</style>