import axios from 'axios'

export const UserMutations = {
  SET_FUNDS: 'SET_FUNDS',
  ADD_FUNDS: 'ADD_FUNDS',
  RET_FUNDS: 'RET_FUNDS',
  SET_USER_INFOS: 'SET_USER_INFOS',
  SET_USER_STATE: 'SET_USER_STATE',
}

export const User = {
  state: {
    user_id: undefined,
    funds : undefined,
    user_stock_infos: undefined
  },
  mutations: {
    [UserMutations.SET_FUNDS](state, newFunds)
    {
      state.funds = newFunds
    }
    ,
    [UserMutations.ADD_FUNDS](state, increment)
    {
      state.funds =  state.funds + increment
    },
    [UserMutations.RET_FUNDS](state, decrement)
    {
      state.funds =  state.funds - decrement
    },
    [UserMutations.SET_USER_STATE](state, userState)
    {
      state.user_id = userState.user_id
      state.funds = userState.funds
      state.user_stock_infos = userState.user_stock_infos
    }
  },
  actions: {
    initUpdateUserState ({commit}, payload) {
      console.log('initializing/updating user state with payload' + payload)
      axios.get('http://0.0.0.0:8080/user', {
        params: payload
      }).then(response =>
       {
         commit(UserMutations.SET_USER_STATE, response.data)
       }
      )
    }

  },
  getters: {
    userState : state => state,
    userFunds : state => state.funds,
    userId: state => state.user_id,
    userStockInfos: state => state.user_stock_infos,
    getUserStock: state => brand => state.user_stock_infos ? state.user_stock_infos.find(el => el.brand == brand) : null,
    getStockQuantity: (state, getters) => brand => {
      const stock = getters.getUserStock(brand)
      return stock ? stock.user_quantity : -1
      }
  }
}

