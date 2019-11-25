<template>
  <div class="profile">
    <h1>This is a profile page</h1>
    <p>{{profile_user}}</p>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import axios from 'axios'
export default {
  name: 'profile',
  props:{
    p_user:{
      type: Object,
      required: false
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
    let selectUserId
    if (!this.p_user){
      selectUserId = this.user.user_id
    }
    else {
      selectUserId = this.p_user.user_id
    }
    axios.get(`http://127.0.0.1:8000/movies/users/${selectUserId}`)
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