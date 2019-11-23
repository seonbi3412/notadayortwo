<template>
  <div class="home">
    <div id="nav">
      <router-link to="/" exact>Home</router-link> |
      <router-link to="/movies">Movies</router-link> |
      <router-link to="/account">Account</router-link> |
       <div v-if="!isAuthenticated">
        <router-link to="/account/login">Login</router-link> |
        <router-link to="/account/signup">Signup</router-link> |
      </div>
      <div v-else>
        <a @click.prevent="logout" href="#">Logout</a>
      </div>
      <router-link to="/community">Community</router-link>
    </div>
    <search-bar @input-change-event="onInputChange"/>
    <movie-list :movies="movies"/>
  </div>
</template>

<script>
// @ is an alias to /src
import SearchBar from '@/components/home/SearchBar.vue'
import MovieList from '@/components/home/MovieList_h.vue'

export default {
  name: 'home',
  components: {
    SearchBar,
    MovieList
  },
  data() {
    return {
      movies: [],
      isAuthenticated: this.$session.has('jwt'),
    }
  },
  methods: {
    onInputChange(value) {
      var router = this.$router
      console.log('searchbar -> home')
      console.log(value)
      router.push({
        name: 'movies',
        params: {movieName:value}
      })
    },
    isLogin() {
      this.$session.start()
      if (this.$session.has('jwt')) {
        this.$store.dispatch('login', this.$session.get('jwt'))
      }
    },
    logout() {
      this.$session.destroy()
      this.$store.dispatch('logout')
      this.isAuthenticated = this.$session.has('jwt')
    },
  },
  updated() {
    this.isAuthenticated = this.$session.has('jwt')
  },
  mounted() {
    this.isLogin()
    this.movies =[{title:'조커', id:1}, {title:'말레피센트', id:2}]
  },
}
</script>