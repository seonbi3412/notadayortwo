<template>
  <div>
    <span v-if="!onOff">
      {{ review.content }} - {{ review.user }} 님
      <button @click="editOn()">수정</button>
      <button @click="deleteReview()">삭제</button>
    </span>
    <span v-else>
      <input type="text" :value="review.content">
      <button @click="editReviewCall">수정</button>
      <button @click="editOn()">취소</button>
    </span>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Review',
  data() {
    return {
      onOff: false
    }
  },
  props: {
    review: {
      type: Object,
      required: true
    }
  },
  methods: {
    deleteReview() {
      axios.delete(`http://127.0.0.1:8000/movies/reviews/${this.review.id}`)
        .then(response => {
          console.log(response)
          this.$emit('delete-event', this.review)
        })
        .catch(error => {
          console.log(error)
        })
    },
    editOn() {
      this.onOff = !this.onOff
    },
    editReviewCall() {
      console.log('수정')
    }
  }
    
}
</script>

<style>

</style>