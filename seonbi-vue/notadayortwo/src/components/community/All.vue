<template>
  <div>
    <h1>
      all page
    </h1>
    <p>{{reviews}}</p>
  </div>
</template>

<script>
export default {
  name: 'all',
  props: {
    reviews:{
      type: Array,
      require: true
    }
  }
}
</script>

<style>

</style>