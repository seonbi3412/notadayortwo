<template>
  <div class="search">
    <!-- <input  type="text" > -->
    <b-form-input placeholder="검색" @change="onInput" v-model="searchInput" list="my-list-id" class="mx-auto my-3" style="width: 400px;"></b-form-input>

    <datalist class="my-5" id="my-list-id">
      <option v-for="movie in movies" :key="`movie-${movie.id}`">{{ movie.title }}</option>
      <option v-for="actor in actors" :key="actor.id">{{ actor.name }} {{actor.id}}</option>
      <option v-for="genre in genres" :key="`genre-${genre.id}`">{{ genre.name }}</option>
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
    },
    genres: {
      type: Array,
      required: true
    },
    actors:{
      type: Array,
      required: true
    },
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
