<template>
  <div class="container box col-7">
    <h1 class="display-1 boxoffice">BoxOffice</h1>
    <div>
      <swiper class="swiper-wrapper" :options="swiperOption" ref="mySwiper">
        <!-- slides -->
        <swiper-slide v-for="movie in boxoffice" :key="movie.movieCd">
          <!-- <div class="title" data-swiper-parallax="-100">{{ movie.rank }}</div> -->
          <div class="poster" data-swiper-parallax="-100"><img v-if="movie.poster_url !== ''" :src="`https://image.tmdb.org/t/p/w300${movie.poster_url}`" alt=""></div>
          <!-- Parallax subtitle -->
          <!-- <div class="subtitle" data-swiper-parallax="-150"><strong>{{ movie.movieNm }}</strong></div> -->
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
          depth: 100,
          modifier: 1,
          slideShadows : false
        },
        parallax: true,
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
    reviews: {
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
  div.container {
    border: 1px solid rgb(10, 10, 10);
    border-radius: 50px;
    padding-left: 15px;
    margin-left: 10px;
    margin-right: 10px;
  }
  .swiper-slide {
    background-position: center;
    background-size: cover;
    background-color: rgba(0, 0, 0, 0);
    width: 300px;
    height: 500px;
  }

  .boxoffice {
  font-family: 'Deco';
  text-align: center;
  font-size: 7em;
  margin: 20px 0 20px 0;
  color: rgb(255, 153, 102);
  }
</style>