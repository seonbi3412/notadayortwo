<template>
  <div class="container">
    <h1 class="display-3">영화 추천</h1>
    <swiper ref="mySwiper">
      <swiperSlide :options="swiperOption" ref="mySwiper" v-for="movie in movies" :key="movie.id">
        <movie-list-item :movie="movie"/>
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
        slidesPerView: 'auto',
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

<style>

</style>