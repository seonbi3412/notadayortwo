<template>
  <swiper :options="swiperOption" ref="mySwiper">
    <!-- slides -->
    <swiper-slide v-for="video in videos" :key="video.id">
      <div>
        <b-embed
          type="iframe"
          aspect="16by9"
          :src="`https://www.youtube.com/embed/${video.key}?rel=0`"
          allowfullscreen
        ></b-embed>
      </div>
    </swiper-slide>
    <!-- Optional controls -->
    <div class="swiper-pagination"  slot="pagination"></div>
    <div class="swiper-button-prev" slot="button-prev"></div>
    <div class="swiper-button-next" slot="button-next"></div>
    <!-- <div class="swiper-scrollbar"   slot="scrollbar"></div> -->
  </swiper>
</template>

<script>
export default {
  name: 'Video',
  props: {
    videos: {
      type: Array
    }
  },
  data() {
    return {
      swiperOption: {
        // swiper 옵션, 콜백함수 모두 동일하게 사용
      },
      pagination: {
        el: '.swiper-pagination'
      }
    }
  }
}
</script>

<style>

</style>