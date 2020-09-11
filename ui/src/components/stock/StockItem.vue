<template>
  <div class="m-4">
    <!-- <div class="w-50"> Hello</div>
    Hello-->
    <b-card
      @blur="init_success_error"
      header-tag="header"
      :header-bg-variant="isBuy ? 'success' :'primary'"
    >
      <template v-slot:header>
        <div class="d-inline h5 card-title mr-2">
          <b>{{myTitle}}</b>
        </div>
        <small v-if="isBuy" class="d-inline">Price ({{price}} $)</small>
        <small v-else class="d-inline">Quantity ({{userQuantity}})</small>
      </template>
      <b-form inline>
        <label class="sr-only" for="inline-form-input-name">Name</label>
        <b-input
          @blur="init_success_error"
          :class="[error ? 'border-danger':'', success ? 'border-success' : '']"
          type="number"
          id="inline-form-input-name"
          class="mb-2 mr-sm-2 mb-sm-0"
          placeholder="Quantity"
          v-model="quantity"
        ></b-input>
        <button v-if="isBuy" @click="operation('buy')" type="button" class="ml-auto btn btn-success">Buy</button>
        <button v-else  @click="operation('sell')" type="button" class="ml-auto btn btn-primary">Sell</button>
      </b-form>
      <p v-if="error" class="text-danger">Something went wrong</p>
      <p v-if="success" class="text-success">Transaction went well</p>
    </b-card>
  </div>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  props: {
    stockInfo: {
      type: Object,
    },
    user_id: {
      type: String,
      default: "Hamza",
    },
    isBuy: {
      type: Boolean,
      default: true,
    },
  },
  data() {
    return {
      quantity: null,
      success: null,
      error: null,
    };
  },
  methods: {
    init_success_error() {
      this.success = null;
      this.error = null;
    },
    operation(operationType='buy') {
      this.init_success_error();
      this.$http
        .post(`http://0.0.0.0:8080/${operationType}`, {
          user_id: this.user_id,
          quantity: this.quantity,
          brand: this.stockInfo.brand,
        })
        .then((response) => {
          if (response.data.success) {
            this.quantity = 0;
            this.success = true;
            this.$store.dispatch("initUpdateUserState", {
              user_id: this.user_id,
            });
          } else {
            this.error = true;
          }
        })
        .catch((error) => {
          this.error = true;
          console.log(error);
        });
    },
  },
  computed: {
    ...mapGetters(["userId", "getStockQuantity", "funds", "userState"]),
    myTitle() {
      return this.stockInfo.brand;
    },
    price() {
      return this.stockInfo.price;
    },
    userQuantity() {
      //console.log(this.userState.user_stock_infos.find(el => el.brand == this.stockInfo.brand))
      return this.getStockQuantity(this.stockInfo.brand);
    },
  },
};
</script>

<style lang="scss" scoped>
</style>
