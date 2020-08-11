<template>
  <div class="m-4">
    <!-- <div class="w-50"> Hello</div>
    Hello-->
    <b-card 
    header-tag="header"
    header-bg-variant="success"
    >
      <template   v-slot:header>
        <div class="d-inline h5 card-title mr-2 "> <b> {{myTitle}}</b></div>
        <small class="d-inline ">Price ({{price}} $)</small>
      </template>
      <b-form inline>
        <label class="sr-only" for="inline-form-input-name">Name</label>
        <b-input
          type="number"
          id="inline-form-input-name"
          class="mb-2 mr-sm-2 mb-sm-0"
          placeholder="Quantity"
          :value="quantity"
        ></b-input>
        <button type="button" class="ml-auto btn btn-success">Buy</button>
      </b-form>
    </b-card>
  </div>
</template>

<script>
export default {
  props: ['stockInfo'],
  data() {
    return {
      quantity: null,

    };
  },
  computed: {
    myTitle() {
      return this.stockInfo.brand;
    },
    price() {
      return this.stockInfo.price
    }
  },
};
</script>

<style lang="scss" scoped>
</style>
