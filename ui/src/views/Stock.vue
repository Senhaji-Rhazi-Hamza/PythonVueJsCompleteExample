
<template>
  <div class="container my-4">
       <!-- <b-card align="left" title="Trade or view your Portfolio" sub-title="Intro">
      <b-card-text>
        You may save & load your Data 
      </b-card-text>
      <hr>
      <b-card-text> <span class="h5"> <b> Your founds.</b></span></b-card-text>

    </b-card> -->
    <stock-items></stock-items>
    <!-- <b-card
        header="featured"
        header-tag="header"
        footer="Card Footer"
        footer-tag="footer"
        title="Title"
      >
        <b-card-text>Header and footers using props.</b-card-text>
        <b-button href="#" variant="primary">Go somewhere</b-button>
      </b-card>
    -->
    <!-- <b-card title="Title" header-tag="header" footer-tag="footer">
        <template v-slot:header>
          <h6 class="mb-0">Header Slot</h6>
        </template>
        <b-card-text>Header and footers using slots.</b-card-text>
        <b-button href="#" variant="primary">Go somewhere</b-button>
        <template v-slot:footer>
          <em>Footer Slot</em>
        </template>
    </b-card>-->
  </div>
</template>

<script>
import StockItems from '../components/stock/StockItems'

export default {

  name: 'Stock',
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
