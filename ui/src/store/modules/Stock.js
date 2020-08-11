import axios from 'axios'

export const StockMutations = {
  STOCKS_UPDATE_INIT: 'STOCKS_UPDATE_INIT',
}

export const Stock = {
  state: {
    stocksInfos: undefined
  },
  getters: {
   stocksInfos: (state) => state.stocksInfos
  },
  mutations: {
    [StockMutations.STOCKS_UPDATE_INIT](state, stocksInfos) {
      state.stocksInfos = stocksInfos
    }
  },
  actions : {
    initUpdateStocks ({commit}) {
      axios.get("http://0.0.0.0:8080/stocks").then((response) => {
         commit(StockMutations.STOCKS_UPDATE_INIT, response.data);
      });
    }
  }
  
}

