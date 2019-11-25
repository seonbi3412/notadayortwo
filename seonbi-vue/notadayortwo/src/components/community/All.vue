<template>
  <div>
    <h1>
      모든 글 목록
    </h1>
    <ul>
      <li v-for="review in reviews" :key="review.id">
        <div>
          <span v-if="!review.updated">
            {{ review.content }} - {{ review.user }} 님
            <button @click="editOn(review)">수정</button>
            <button @click="deleteReview(review)">삭제</button>
          </span>
          <span v-else>
            <input type="text" :value="review.content">
            <button @submit.prevent="editReviewCall(review)">수정</button>
            <button @click="editOn(review)">취소</button>
          </span>
        </div>
      </li>
    </ul>
    <p>{{reviews}}</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'all',
  props: {
    reviews:{
      type: Array,
      require: true
    }
  },
  data() {
    return {
      
    }
  },
  methods: {
    deleteReview(review) {
      axios.delete(`http://127.0.0.1:8000/movies/reviews/${review.id}/`)
        .then(response => {
          console.log(response)
          const idx = this.reviews.indexOf(review)
          if (idx > -1) {
            this.reviews.splice(idx, 1)
          }
        })
        .catch(error => {
          console.log(error)
        })
    },
    editOn(review) {
      const idx = this.reviews.indexOf(review)
      this.$set(this.reviews[idx], 'updated', !review.updated)
      console.log(this.reviews[idx])
    },
    editReviewCall(review) {
      axios.put(`http://127.0.0.1:8000/movies/reviews/${review.id}/`)
        .then(response => {
          console.log(response)
        })
        .catch(error => {
          console.log(error)
        })
      console.log('수정')
    }
  }
}
</script>

<style>
</style>