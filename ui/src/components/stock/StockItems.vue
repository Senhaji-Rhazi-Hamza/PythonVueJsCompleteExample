
<template>
  <div class="row">
    
    <!-- <stock-item class="col-sm-6" v-for="stockInfo in stocksInfos" :key="stockInfo.id"> </stock-item> -->
    <div class="col-sm-6" v-for="stockInfo in stocksInfos" :key="stockInfo.id">
      <stock-item :isBuy="isBuy" :stock-info="stockInfo"></stock-item>
    </div>
  </div>
</template>

<script>
import StockItem from "./StockItem.vue";

export default {
  props: {
    isBuy: {
      type: Boolean,
      default: true,
    },
  },
  components: {
    StockItem,
  },
  computed: {
    stocksInfos () {
      return this.$store.getters.stocksInfos
    }
  },
  created() {
    this.$store.dispatch('initUpdateStocks')
  },
};
</script>

<style lang="scss" scoped>
</style>
