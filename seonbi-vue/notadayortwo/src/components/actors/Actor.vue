<template>
  <div class="actor container d-flex justify-content-center align-items-center">
    <div class="col-4">
      <h1>{{ actor.name }}</h1>
      <img :src="profile_path" :alt="actor.name">
    </div>
    <div class="col-8 d-flex flex-column">
      <h5>필모그래피 : <li v-for="filmo in actor.filmography" :key="filmo.id">{{ filmo.title }} </li></h5>
      <p>{{ like_count }}</p>
      <div class="container">
        <button class="btn btn-secondary" @click="likeActor" v-if="!isLiked && this.user">좋아요</button>
        <button class="btn btn-secondary" @click="likeActor" v-else-if="this.user">좋아요 취소</button>
      </div>
      <div class="container">
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapGetters } from 'vuex'
export default {
  name: "actor",
data() {
    return {
      actor: {},
      profile_path: "",
      isLiked: false,
      like_count: 0,
    }
  },
  computed: {
    ...mapGetters([
      'options',
      'user'
    ]),
  },
  methods: {
    likeActor() {
      axios.post(`http://127.0.0.1:8000/movies/actors/${this.actor.id}/like/`, this.user, this.options)
        .then(response => {
          this.actor = response.data
          this.like_count = this.actor.like_users.length
          this.isLiked = false
          for(let idx in this.actor.like_users){
            if (this.actor.like_users[idx].id === this.user.user_id){
              this.isLiked = true
              break
            }
          }
          this.$emit('redataload', true)
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  mounted() {
    axios.get(`http://127.0.0.1:8000/movies/actors/${this.$route.params.id}/`)
      .then(response => {
        this.actor = response.data
        this.like_count = this.actor.like_users.length
        this.profile_path=`https://image.tmdb.org/t/p/w300${this.actor.profile_path}`
        this.isLiked = false
          for(let idx in this.actor.like_users){
            if (this.actor.like_users[idx].id === this.user.user_id){
              this.isLiked = true
              break
            }
          }
        })
      .catch(error => {
        console.log(error)
      })
  }
}
</script>

<style>

</style>