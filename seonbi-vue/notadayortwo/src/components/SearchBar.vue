<template>
  <div class="search">
    <h1>검색 바</h1>
    <input @change="onInput" v-model="searchInput" type="text" class="my-3">
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  data() {
    return {
      searchInput: ""
    }
  },
  methods: {
    onInput(event) {
      this.$emit('input-change-event', event.target.value)
      this.searchInput = ""
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
