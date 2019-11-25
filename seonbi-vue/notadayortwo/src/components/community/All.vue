<template>
  <div>
    <h1>
      모든 글 목록
    </h1>
    <li v-for="review in reviews" :key="review.id">
      <Review :review="review" @delete-event="deleteReview"/>
    </li>
  </div>
</template>

<script>
import Review from './Review.vue'

export default {
  name: 'all',
  data() {
    return {
      
    }
  },
  props: {
    reviews:{
      type: Array,
      require: true
    }
  },
  components: {
    Review
  },
  methods: {
    deleteReview(review) {
      console.log(review)
      const idx = this.reviews.indexOf(review)
      console.log(idx)
      if (idx > -1) {
        console.log(this.reviews)
        this.reviews.splice(idx, 1)
        console.log(this.reviews)
      }
    }
  }
}
</script>

<style>

</style>