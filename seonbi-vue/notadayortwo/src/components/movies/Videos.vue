<template>
  <swiper :options="swiperOption" ref="mySwiper">
    <!-- slides -->
    <swiper-slide v-for=" video in videoList" :key="video">
      <iframe width="640" height="360" :src="`${video}?controls=0`" frameborder="0" allow="autoplay;"></iframe>
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
  name: 'Videos',
  props: {
    pvideos: {
      type: String,
    }
  },
  data() {
    return {
      swiperOption: {
        // swiper 옵션, 콜백함수 모두 동일하게 사용
        slidePerView: 1,
        loop: true,
        navigation: {
          nextEl: '.swiper-button-next',
          prevEl: '.swiper-button-prev',
        }
      },
      videoList: []
    }
  },
  methods: {
    // videoList() {
    //   if(this.pvideos)
    //   return this.
    // }
  },
  mounted() {
    if(this.$props.pvideos){
      this.videoList = this.$props.pvideos.split(" ")
    }

  },
}
</script>

<style>

</style>