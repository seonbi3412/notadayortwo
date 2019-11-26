<template>
  <div class="profile">
    <h1>This is a profile page</h1>
    <p>{{profile_user.id}}</p>
    <p>{{profile_user.username}}</p>
    <ul>
      <li v-for="movie in profile_user.like_movies" :key="movie.id">
        {{movie.title}}
      </li>
    </ul>
    <b-button to="/account/edit" v-if="this.user.user_id===profile_user.id">edit</b-button>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import axios from 'axios'
export default {
  name: 'profile',
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
  },
  data() {
    return {
      profile_user: {}
    }
  },
  computed: {
    ...mapGetters([
      'options',
      'user'
    ])
  },
  mounted() {
    axios.get(`http://127.0.0.1:8000/movies/users/${this.$route.params.id}`)
        .then(response => {
          console.log(response)
          this.profile_user = response.data
        })
        .catch(error => {
          console.log(error)
        })
  }
}
</script>

<style>

</style>