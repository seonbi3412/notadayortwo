<template>
  <div class="account">
    <h1>This is a account page</h1>
    <router-view :genres="genres" :users="users"/>
  </div>
</template>
<script>
export default {
  props:{
    movies: {
      type: Array,
      required: true
    },
    genres: {
      type: Array,
      required: true
    },
    users: {
      type:Array,
      required:true
    }
  }
}
</script>

<style>

</style>