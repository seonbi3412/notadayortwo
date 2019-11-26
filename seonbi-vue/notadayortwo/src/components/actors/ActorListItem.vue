<template>
  <div class="actorlistitem">
    <router-link :to="`/actors/${actor.id}`">
    {{actor.name}}
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
</style>