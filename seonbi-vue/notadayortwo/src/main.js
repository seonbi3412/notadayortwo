import Vue from 'vue'
import VueSession from 'vue-session'
import App from './App.vue'
import router from './router'
import store from './store'
import BootstrapVue from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import VueAwesomeSwiper from 'vue-awesome-swiper'

// require styles
import 'swiper/dist/css/swiper.css'

import { library } from '@fortawesome/fontawesome-svg-core'
import { faUserSecret, faTrashAlt, faPen } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faUserSecret, faTrashAlt, faPen)

Vue.component('font-awesome-icon', FontAwesomeIcon)

Vue.use(VueAwesomeSwiper, /* { default global options } */)
Vue.config.productionTip = false
Vue.use(VueSession)
Vue.use(BootstrapVue)
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')