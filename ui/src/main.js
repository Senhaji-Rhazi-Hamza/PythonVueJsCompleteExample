import Vue from 'vue'
import App from './App.vue'

import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import { router } from './router'
import axios from 'axios'
import { store } from './store/store'

//import './custom.scss'


Vue.prototype.$http = axios
// Install BootstrapVue
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)

Vue.config.productionTip = false

new Vue({
  store,
  router,
  created() {

   this.$store.dispatch('initUpdateUserState', {
     user_id: 'Hamza'
   })
  },
  render: h => h(App),
}).$mount('#app')
