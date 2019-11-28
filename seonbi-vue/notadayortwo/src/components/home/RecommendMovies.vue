<template>
  <div class="container rec col-3">
    <h1 class="display-1 neon">Recommended</h1>
    <swiper ref="mySwiper">
      <swiperSlide :options="swiperOption" ref="mySwiper" v-for="movie in movies" :key="movie.id">
        <movie-list-item :movie="movie" :reviews="reviews" :users="users"/>
      </swiperSlide>

      <div class="swiper-pagination"  slot="pagination"></div>
    </swiper>
  </div>
</template>

<script>
import MovieListItem from '@/components/movies/MovieListItem.vue'
import 'swiper/dist/css/swiper.css'
import { swiper, swiperSlide } from 'vue-awesome-swiper'
export default {
  name: 'recommendMovies',
  data() {
    return {
      swiperOption: {
        // swiper 옵션, 콜백함수 모두 동일하게 사용
        effect: 'coverflow',
        slidesPerView: 4,
        spaceBetween: 30,
        autoplay: {
          delay: 5000,
          stopOnLastSlide: false,
          disableOnInteraction: false,
          reverseDirection: false,
        }
      },
      pagination: {
        el: '.swiper-pagination',
      }
    }
  },
  props: {
    movies: {
      type: Array,
      required: true
    },
    reviews: {
      type: Array,
      required: true
    },
    users: {
      type: Array,
      required: true
    }
  },
  components: {
    swiper,
    swiperSlide,
    MovieListItem
  },
  computed: {
    swiper() {
      return this.$refs.mySwiper.swiper
    }
  },
  mounted() {
    this.swiper.slideTo(1, 1000, false)
  }
}
</script>

<style scoped>
  div.container {
    background-color: rgba(0, 0, 0, 0.438);
    border-radius: 50px;
    padding-left: 15px;
  }
  .swiper-slide {
    background-position: center;
    background-size: cover;
    background-color: rgba(0, 0, 0, 0);
    width: 300px;
    height: 500px;
  }
  .neon {
    color: rgb(204, 153, 255);
    font-family: 'Deco';
    text-align: center;
    font-size: 7em;
    margin: 20px 0 20px 0;
  }
</style>