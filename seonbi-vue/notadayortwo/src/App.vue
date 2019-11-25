<template>
  <div id="app">
    <div v-if="!this.$route.path.includes('account')">
      <Nav/>
    </div>
    <router-view :movies="movies"/>
  </div>
</template>

<script>
// @ is an alias to /src
import Nav from './views/Nav.vue'
import { mapGetters } from 'vuex'
import axios from 'axios'

export default {
  name: 'app',
  components: {
    Nav
  },
  data() {
    return {
      movies: [],
    }
  },
  computed: {
    ...mapGetters([
      'options',
      'user'
    ])
  },
  mounted() {
    axios.get(`http://127.0.0.1:8000/movies/`)
    .then(response =>{
      this.movies = response.data
    })
    .catch(error => {
      console.log(error)
    })
  },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>