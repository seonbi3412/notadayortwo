<template>
  <swiper class="gt" :options="swiperOption" ref="mySwiper" @someSwiperEvent="callback">
    <!-- slides -->
    <swiper-slide v-for="movie in movies" :key="movie.id"><movie-list-item :movie="movie"/></swiper-slide>
    <!-- Optional controls -->
    <div class="swiper-pagination"  slot="pagination"></div>
    <div class="swiper-button-prev" slot="button-prev"></div>
    <div class="swiper-button-next" slot="button-next"></div>
    <!-- <div class="swiper-scrollbar"   slot="scrollbar"></div> -->
  </swiper>
</template>

<script>
import 'swiper/dist/css/swiper.css'
import { swiper, swiperSlide } from 'vue-awesome-swiper'
import MovieListItem from './movies/MovieListItem.vue'

export default {
  name: 'carrousel',
  data() {
    return {
      swiperOption: {
        // swiper 옵션, 콜백함수 모두 동일하게 사용
        effect: 'coverflow',
        grabCursor: true,
        centeredSlides: true,
        slidesPerView: 'auto',
        coverflowEffect: {
          rotate: 40,
          stretch: 0,
          depth: 100,
          modifier: 1,
          slideShadows : true
        }
      },
      pagination: {
            el: '.swiper-pagination'
      }
    }
  },
  props: {
    movies: {
      type: Array,
      required: true
    }
  },
  computed: {
    swiper() {
      return this.$refs.mySwiper.swiper
    }
  },
  mounted() {
    // 현재 swiper 인스턴스를 확인
    console.log('this is current swiper instance object', this.swiper)
    this.swiper.slideTo(3, 1000, false)
  },
  components: {
    swiper,
    swiperSlide,
    MovieListItem
  }
}
</script>

<style scoped>
  .swiper-slide {
    background-position: center;
    background-size: cover;
    background-color: rgba(0, 0, 0, 0);
    width: 300px;
    height: 600px;
  }
</style>