<template>
  <div>
    <h1>
      모든 글 목록
    </h1>
    <li v-for="review in reviews" :key="review.id">
      {{ review.content }} - {{ review.user }} 님
      <button @click="editReview()">수정</button>
      <button @click="deleteReview(review)">삭제</button>
    </li>
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
  methods: {
    deleteReview(review) {
      console.log(`http://127.0.0.1:8000/movies/reviews/${review.id}`)
      axios.delete(`http://127.0.0.1:8000/movies/reviews/${review.id}`)
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
    editReview() {
      console.log('수정버튼')
    }
  }
}
</script>

<style>

</style>