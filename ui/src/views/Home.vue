<template>
  <div class="container my-4"  >
    <b-card align="left" title="Trade or view your Portfolio" sub-title="Intro">
      <b-card-text>
        You may buy and sell stock options, you have a view for selling stocks  (Portfolio view) and 
        a view for buying stocks (Stock view) when ever you hit the right side menu button <b>End the day</b> the 
        stock prices get updated in real time randomly by +- 33% 
      </b-card-text>
      <hr>
      <b-card-text> <span class="h5"> <b> Your actual funds. {{funds | round}}</b></span></b-card-text>

    </b-card>
  </div>
</template>

<script>
export default {
  computed: {
    funds () {
      return this.$store.getters.userState.funds
    }
  },
};
</script>

<style lang="scss" scoped>
</style>
