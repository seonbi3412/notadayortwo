<template>
  <div class="container">
    <div class="row">
      <div class="chat container border my-3 px-1">
        <div v-for="review in reviews" :key="review.id">
          <p v-if="review.movie_id">{{ review.content }}</p>
          
        </div>
      </div>
      <div class="chat container border my-3 px-1"> <!-- 영화없는 댓글 -->
        <div class="d-flex justify-content-start" v-for="review in reviews" :key="review.id">
          <div v-if="user.user_id !== review.user.id" class="userThumb col-1 d-flex align-items-center">
            <p class="m-0">{{ review.user.username }}</p>
          </div>
          <div class="col-9 d-flex align-items-center" :class="{ chatBubble_u: user.user_id !== review.user.id, chatBubble_m: user.user_id === review.user.id }" v-if="!review.updated">
            <p class="m-0">{{ review.content }}</p>
            <a class="edit_delete" href="" @click.prevent="editOn(review)" v-if="user.user_id === review.user.id"><font-awesome-icon icon="pen" size="xs"/></a>
            <a class="edit_delete" href="" @click.prevent="deleteReview(review)" v-if="user.user_id === review.user.id"><font-awesome-icon icon="trash-alt" size="xs"/></a>
          </div>
          <form v-else>
            <input type="text" v-model="editContent">
            <button class="btn btn-light" @click.prevent="editReview(review)" v-if="review.movie_id">리뷰</button>
            <button class="btn btn-light" @click.prevent="editArticle(review)" v-else>댓글</button>
            <button class="btn btn-light" @click.prevent="editOn(review)">취소</button>
          </form>
        </div>
      <form class="col-12 my-3" @submit.prevent="createReview" v-if="user">
        <input type="text" v-model="content">
        <button type="submit">등록</button>
      </form>
      </div> <!-- 영화없는 댓글 -->
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapGetters } from 'vuex'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

export default {
  name: 'all',
  data() {
    return {
      content: '',
      editContent: '',
      tmp_review: {},
      is_me: true
    }
  },
  components: {
    FontAwesomeIcon
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
        'user': this.user.user_id
      }
      axios.post(`http://127.0.0.1:8000/movies/articles/`, data, this.options)
        .then(response => {
          console.log(response)
          this.tmp_review = response.data
          this.users.forEach(user => {
            if (user.id === response.data.user) {
              this.tmp_review.user = user
            }
          })
          this.reviews.push(this.tmp_review)
          this.content = ''
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
      this.editContent = review.content
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
        'content': this.editContent,
        'user': review.user.id
      }
      axios.put(`http://127.0.0.1:8000/movies/articles/${review.id}/`, data, this.options)
        .then(response => {
          console.log(response)
          return response.data
        })
        .then(data => {
          const idx = this.reviews.indexOf(review)
          this.$set(this.reviews[idx], 'updated', !review.updated)
          this.$set(this.reviews[idx], 'content', data.content)
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>

<style>
div.userThumb {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  border: 1px solid black;
  margin: 15px;
}
div.chat {
  width: 500px;
  height: 800px;
  border-radius: 30px;
  background-color: rgb(230, 230, 230);
  overflow-y: scroll;
}
div.chatBubble_u {
  position:relative;
  margin-top: 15px;
  margin-bottom: 15px;
  margin-left: 5px;
  margin-right: auto;
  padding: 5px;
  width: 300px; 
  background: rgb(250, 250, 250); 
  border-radius: 10px;
}
div.chatBubble_u::before {
  border-top: 5px solid transparent; 
  border-left: 0px solid transparent; 
  border-right: 15px solid rgb(250, 250, 250); 
  border-bottom: 10px solid transparent; 
  content:""; 
  position:absolute;
  top: 20px;
  left: -15px;
}
div.chatBubble_m {
  position:relative;
  margin-top: 15px;
  margin-right: 15px;
  margin-bottom: 15px;
  margin-left: auto;
  padding: 5px;
  width: 300px; 
  background: rgb(255, 240, 155); 
  border-radius: 10px;
}
div.chatBubble_m::after {
  border-top: 10px solid transparent; 
  border-left: 18px solid rgb(255, 240, 155); 
  border-right: 0px solid transparent; 
  border-bottom: 5px solid transparent; 
  content:""; 
  position:absolute;
  top: 15px;
  right: -15px;
}
a.edit_delete {
  text-decoration: none;
  color: darkgray;
}
a.edit_delete:hover {
  color: black;
}
</style>