<template>
  <div class="account">
    <router-view :genres="genres" :users="users" @redataload="loadDBdata"/>
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
  methods: {
    loadDBdata() {
      this.$emit('redataload', true)
    }
  }
}
</script>
<style>

</style>