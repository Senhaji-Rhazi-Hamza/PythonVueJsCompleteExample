
<template>
  <div class="row" >

      <!-- <stock-item class="col-sm-6" v-for="stockInfo in stocksInfos" :key="stockInfo.id"> </stock-item> -->
    <div class="col-sm-6"  v-for="stockInfo in stocksInfos" :key="stockInfo.id"> <stock-item :stock-info="stockInfo" > </stock-item>  </div>

  </div>
</template>

<script>
import StockItem from './StockItem.vue'

export default {
  components : {
    StockItem
  },
  data() {
    return {
      stocksInfos: [
        { id: 1, brand: "BMW", price: "100", quantity: "100" },
        { id: 2, brand: "Mercedes", price: "100", quantity: "100" },
         { id: 3, brand: "Mercedes", price: "100", quantity: "100" },
      ],
    };
  },
};
</script>

<style lang="scss" scoped>
</style>
