<template>
  <div class="search">
    <h1>검색 바</h1>
    <!-- <input  type="text" > -->
    <b-form-input @change="onInput" v-model="searchInput" list="my-list-id" class="mt-2"></b-form-input>

    <datalist id="my-list-id">
      <option>Manual Option</option>
      <option v-for="movie in movies" :key="movie.id">{{ movie.title }}</option>
    </datalist>
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  data() {
    return {
      searchInput: "",
    }
  },
  props: {
    movies: {
      type: Array,
      required: true
    }
  },
  methods: {
    onInput(event) {
      console.log(event)
      this.$emit('input-change-event', event)
      this.searchInput = ""
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
