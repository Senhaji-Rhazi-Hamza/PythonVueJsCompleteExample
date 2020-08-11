
<template>
  <div class="container my-4">
    <stock-items :isBuy="false" ></stock-items>

  </div>
</template>

<script>
import StockItems from '../components/stock/StockItems'

export default {

  name: 'Portfolio',
  components: {
   StockItems
  },
  data() {
    return {
      
    };
  },
};
</script>

<style lang="scss" scoped>
</style>
