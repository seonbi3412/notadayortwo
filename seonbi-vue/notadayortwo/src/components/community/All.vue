<template>
  <div>
    <h1>
      모든 글 목록
    </h1>
    <form @submit.prevent="createReview" v-if="user">
      <input type="text" v-model="content">
      <input type="number" v-model="score">
      <button type="submit">등록</button>
    </form>
    <li v-for="review in reviews" :key="review.id">
      <div>
        <span v-if="!review.updated">
          {{ review.score }} | 
          {{ review.content }} - {{ review.user.username }} 님
          <span v-if="review.movie_id">
            {{review.movie_id}}
            <p>있고</p>
          </span>
          <span v-else>
          <p>없고</p>
          </span>
          <button @click="editOn(review)" v-if="user.user_id === review.user.id">수정</button>
          <button @click="deleteReview(review)" v-if="user.user_id === review.user.id">삭제</button>
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
  </div>
</template>

<script>
import axios from 'axios'
import { mapGetters } from 'vuex'
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
      require: true,
    },
    users:{
      type: Array,
      required: true
    },
  },
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
        'user': this.user.user_id
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
        .then(response => {
          console.log(response)
          const idx = this.reviews.indexOf(review)
          if (idx > -1) {
            this.reviews.splice(idx, 1)
            alert(response.data.message)
          }
        })
        .catch(error => {
          console.log(error)
        })
    },
    editOn(review) {
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
    }
  }
}
</script>

<style>
</style>