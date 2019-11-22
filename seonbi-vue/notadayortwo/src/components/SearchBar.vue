<template>
  <div class="search">
    <h1>메인화면 검색 바</h1>
    <input @change="onInput" type="text" class="my-3">
  </div>
</template>

<script>
export default {
  name: 'SearchBar',
  methods: {
    onInput(event) {
      console.log('==SearchBar==')
      console.log(event.target.value)
      // $emit(이벤트이름, 값) : 커스텀 이벤트 발생
      // 이벤트이름의 이벤트를 발생 시킴(트리거)
      this.$emit('input-change-event', event.target.value)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
