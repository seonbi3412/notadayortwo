<template>
  <div>
    <h1>
      모든 글 목록
    </h1>
<<<<<<< HEAD
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
=======
    <form @submit.prevent="createReview" v-if="this.user">
      <input type="text" v-model="content">
      <input type="number" v-model="score">
      <button type="submit">등록</button>
    </form>
    <li v-for="review in reviews" :key="review.id">
      <div>
        <span v-if="!review.updated">
          {{ review.score }} | 
          {{ review.content }} - {{ review.user }} 님
          <span v-if="review.movie_id">
            {{review.movie_id}}
            <p>있고</p>
          </span>
          <span v-else>
          <p>없고</p>
          </span>
          <button @click="editOn(review)">수정</button>
          <button @click="deleteReview(review)">삭제</button>
        </span>
        <form v-else>
          <input type="number" v-model="review.score">
          <input type="text" v-model="review.content">
          <button @click.prevent="editReview(review)" v-if="review.movie_id">리뷰</button>
          <button @click.prevent="editArticle(review)" v-else>댓글</button>
          <button @click.prevent="editOn(review)">취소</button>
        </form>
      </div>
    </li>
>>>>>>> seon
  </div>
</template>

<script>
import axios from 'axios'
<<<<<<< HEAD
=======
import { mapGetters } from 'vuex'
>>>>>>> seon

export default {
  name: 'all',
  data() {
    return {
      content: '',
      score: 0,
    }
  },
  props: {
    reviews:{
      type: Array,
      require: true
    }
  },
<<<<<<< HEAD
  data() {
    return {
      
    }
  },
  methods: {
    deleteReview(review) {
      axios.delete(`http://127.0.0.1:8000/movies/reviews/${review.id}/`)
=======
  computed: {
    ...mapGetters([
      'options',
      'user'
    ])
  },
  methods: {
    createReview() {
      const data = {
        'content': this.content,
        'score': this.score,
        'user': this.user
      }
      axios.post(`http://127.0.0.1:8000/movies/articles/`, data, this.options)
        .then(response => {
          console.log(response)
          this.reviews.push(response.data)
        })
        .catch(error => {
          console.log(error)
        })
    },
    deleteReview(review) {
      axios.delete(`http://127.0.0.1:8000/movies/reviews/${review.id}/`, this.options)
>>>>>>> seon
        .then(response => {
          console.log(response)
          const idx = this.reviews.indexOf(review)
          if (idx > -1) {
            this.reviews.splice(idx, 1)
<<<<<<< HEAD
=======
            alert(response.data.message)
>>>>>>> seon
          }
        })
        .catch(error => {
          console.log(error)
        })
    },
    editOn(review) {
<<<<<<< HEAD
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
=======
      console.log(this)
      const idx = this.reviews.indexOf(review)
      this.$set(this.reviews[idx], 'updated', !review.updated)
    },
    editReview(review) {
      
      const data = {
        'score': review.score,
        'content': review.content,
        'movie_id': review.movie_id,
        'user': review.user 
      }
      console.log('Review')
      axios.put(`http://127.0.0.1:8000/movies/reviews/${review.id}/`, data, this.options)
        .then(response => {
          console.log(response)
        })
        .then(() => {
          const idx = this.reviews.indexOf(review)
          this.$set(this.reviews[idx], 'updated', !review.updated)
        })
        .catch(error => {
          console.log(error)
        })
    },
    editArticle(review) {
      
      const data = {
        'score': review.score,
        'content': review.content,
        'user': review.user
      }
      axios.put(`http://127.0.0.1:8000/movies/articles/${review.id}/`, data, this.options)
        .then(response => {
          console.log(response)
        })
        .then(() => {
          const idx = this.reviews.indexOf(review)
          this.$set(this.reviews[idx], 'updated', !review.updated)
        })
        .catch(error => {
          console.log(error)
        })
>>>>>>> seon
    }
  }
}
</script>

<style>
</style>