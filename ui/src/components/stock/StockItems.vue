
<template>
  <div class="row">
    <!-- <stock-item class="col-sm-6" v-for="stockInfo in stocksInfos" :key="stockInfo.id"> </stock-item> -->
    <div class="col-sm-6" v-for="stockInfo in stocksInfos" :key="stockInfo.id">
      <stock-item :stock-info="stockInfo"></stock-item>
    </div>
  </div>
</template>

<script>
import StockItem from "./StockItem.vue";

export default {
  components: {
    StockItem,
  },
  data() {
    return {
      stocksInfos: [],
    };
  },
  methods: {
    update_stocks() {
      this.$http.get("http://0.0.0.0:8080/stocks").then((response) => {
        this.stocksInfos = response.data;
      });
    },
  },
  created() {
    this.update_stocks();
  },
};
</script>

<style lang="scss" scoped>
</style>
