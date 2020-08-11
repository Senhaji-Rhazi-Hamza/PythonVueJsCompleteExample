<template>
 <div class="container" >
   <b-navbar toggleable="lg" type="light" variant="fade" >
    <b-navbar-brand to="/">Stock Treader</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item to="/portfolio"> Portfolio</b-nav-item>
        <b-nav-item to="/stock"> Stock</b-nav-item>

      </b-navbar-nav>
        
      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <!-- <b-nav-form>
          <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
          <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
        </b-nav-form> -->
        <b-nav-item @click="update_stock_prices" href="#" right> Ends the day </b-nav-item>

        <b-nav-item  href="#" right>Funds  ({{funds}})</b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
         <!-- <router-view></router-view> -->
 </div>
</template>

<script>

export default {
  computed: {
    funds () {
      return this.$store.getters.userState.funds
    },
    user_id ()
    {
          return this.$store.getters.userState.user_id
    }
  },

  methods: {
    update_stock_prices () {
      this.$http.post('http://0.0.0.0:8080/update_stocks')
      this.$store.dispatch("initUpdateUserState", {
              user_id: this.user_id,
            })
      this.$store.dispatch('initUpdateStocks')
    }
  },
}

</script>

<style lang="scss" scoped>
 .navbar {
   background-color: #ebf3f3;
 }
</style>
