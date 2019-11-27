<template>
  <div class="actorlistitem">
    <router-link :to="`/actors/${actor.id}`">
      <img v-if="actor.profile_path" :src="`https://image.tmdb.org/t/p/w200${actor.profile_path}`" alt="" style="width:100%">
      <img v-else src="../../assets/profile.jpg" alt="no-profile" style="width:100%">
    </router-link>
  </div>
</template>

<script>

export default {
  name: "actorListItem",
  data() {
    return {
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
  width: 100%;
  height: 100%;
}
</style>