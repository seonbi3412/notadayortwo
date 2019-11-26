<template>
  <div class="container">
    <h1 class="display-3">Boxoffice</h1>
    <div>
      <swiper class="swiper-wrapper" :options="swiperOption" ref="mySwiper">
        <!-- slides -->
        <swiper-slide v-for="movie in boxoffice" :key="movie.movieCd">
          <div class="title" data-swiper-parallax="-100">{{ movie.rank }}</div>
          <img v-if="movie.poster_url !== ''" :src="`https://image.tmdb.org/t/p/w300${movie.poster_url}`" alt="">
          <!-- Parallax subtitle -->
          <div class="subtitle" data-swiper-parallax="-200">{{ movie.movieNm }}</div>
          <!-- And parallax text with custom transition duration -->
        </swiper-slide>
        <!-- Optional controls -->
        <div class="swiper-pagination"  slot="pagination"></div>
        <!-- <div class="swiper-scrollbar"   slot="scrollbar"></div> -->
      </swiper>
    </div>
  </div>
</template>

<script>
import 'swiper/dist/css/swiper.css'
import { swiper, swiperSlide } from 'vue-awesome-swiper'
// import MovieListItem from './movies/MovieListItem.vue'

export default {
  name: 'carousel',
  data() {
    return {
      swiperOption: {
        // swiper 옵션, 콜백함수 모두 동일하게 사용
        effect: 'coverflow',
        grabCursor: true,
        centeredSlides: true,
        slidesPerView: 'auto',
        coverflowEffect: {
          rotate: 10,
          stretch: 0,
          depth: 200,
          modifier: 1,
          slideShadows : false
        },
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
    boxoffice: {
      type: Array,
      required: true
    },
  },
  computed: {
    swiper() {
      return this.$refs.mySwiper.swiper
    }
  },
  mounted() {
    // 현재 swiper 인스턴스를 확인
    console.log('this is current swiper instance object', this.swiper)
    this.swiper.slideTo(1, 1000, false)    
  },
  components: {
    swiper,
    swiperSlide,
    // MovieListItem
  }
}
</script>

<style scoped>
  .swiper-slide {
    background-position: center;
    background-size: cover;
    background-color: rgba(0, 0, 0, 0);
    width: 300px;
    height: 500px;
  }
</style>