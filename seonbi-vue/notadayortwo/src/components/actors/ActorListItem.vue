<template>
  <div class="actorlistitem d-flex align-items-center">
    <router-link :to="`/actors/${actor.id}`" class="text-dark">
      <img v-if="actor.profile_path" :src="`https://image.tmdb.org/t/p/w200${actor.profile_path}`" alt="">
      <img v-else src="../../assets/profile.jpg" alt="no-profile">
      <p>{{actor.name}}</p>
    </router-link>
  </div>
</template>

<script>

export default {
  name: "actorListItem",
  data() {
    return {
      // posterUrl: `https://image.tmdb.org/t/p/w300${this.movie.poster_url}`
    }
  },
  props: {
    actor: {
      type: Object,
      required: true
    }
  },
}
</script>

<style>
div.actorlistitem {
  width: 200px;
  height: 320px;
}
</style>