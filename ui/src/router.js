import Vue from 'vue'
import VueRouter from 'vue-router'

import Portfolio from "./views/Portfolio"
import Stock from "./views/Stock"
import Home from "./views/Home"

const router = new VueRouter({
  routes: [
    {path: '/portfolio', name: 'portfolio', component: Portfolio},
    {path: '/stock', name: 'stock', component: Stock},
    {path: '/', name: 'home', component: Home}
  ]
})

Vue.use(VueRouter)

export { router }
