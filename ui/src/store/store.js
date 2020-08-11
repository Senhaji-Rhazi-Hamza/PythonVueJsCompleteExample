import Vue from 'vue'
import Vuex from 'vuex'
import { User, UserMutations } from './modules/User'
import { Stock, StockMutations } from './modules/Stock'

Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    user: User,
    stock: Stock,
  }
})

export { store }
export { UserMutations }
export { StockMutations }
