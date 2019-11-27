<template>
  <div>
    <b-navbar type="dark" variant="dark">
      <b-navbar-brand class="col-1" to="/" exact>Seonbi</b-navbar-brand>
      <b-navbar-nav class="col-6 d-flex justify-content-start">
        <b-nav-item to="/movies" class="btn">Movies</b-nav-item>
        <b-nav-item to="/community" class="btn">Community</b-nav-item>
      </b-navbar-nav>
      <b-navbar-nav class="col-3">
        <b-collapse id="collapse-1" class="mt-2">
          <b-nav-form v-if="this.$route.name !== 'search'" @submit.prevent="onInputChange">
            <b-form-input class="search mr-sm-2" placeholder="Search"></b-form-input>
            <b-button variant="secondary" class="my-2 my-sm-0" type="submit">Search</b-button>
          </b-nav-form>
        </b-collapse>
      </b-navbar-nav>
      <b-navbar-nav class="col-2 btn d-flex justify-content-end">
        <b-button v-b-toggle.collapse-1 v-if="this.$route.name !== 'search'" variant="light" class="btn-sm mr-3"><font-awesome-icon icon="search" size="md"/></b-button>
        <b-nav-item v-if="!isAuthenticated" to="/account/login">Login</b-nav-item>
        <b-nav-item v-if="!isAuthenticated" to="/account/signup">Signup</b-nav-item>
        <b-nav-item v-if="isAuthenticated" :to="`/account/profile/${this.user.user_id}`">{{this.user.username}}</b-nav-item>
        <b-nav-item v-if="isAuthenticated" to="/" @click.prevent="logout">Logout</b-nav-item>
      </b-navbar-nav>
    </b-navbar>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

export default {
    name: 'Nav',
    data() {
    return {
      movies: [],
      isAuthenticated: this.$session.has('jwt'),
    }
  },
  props: {
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
    onInputChange(event) {
      console.log(event.target[0].value)
      var router = this.$router
      router.push({
        name: 'search',
        params: {movieName:event.target[0].value}
      })
    },
  },
  computed: {
    ...mapGetters([
      'options',
      'user'
    ])
  },
  mounted() {
    this.isLogin()
  },
  components: {
    FontAwesomeIcon
  }
}
</script>

<style scoped>
  div {
    font-family: 'Komika Boogie', '배달의민족 주아';
    letter-spacing: 4px;
    color: aquamarine;
  }
</style>