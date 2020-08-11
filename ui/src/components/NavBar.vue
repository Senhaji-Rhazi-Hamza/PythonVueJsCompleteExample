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
          <b-nav-item href="#">End Day</b-nav-item>
        <b-nav-item-dropdown text="Save & load" right>
          <b-dropdown-item href="#">EN</b-dropdown-item>
          <b-dropdown-item href="#">ES</b-dropdown-item>
          <b-dropdown-item href="#">RU</b-dropdown-item>
          <b-dropdown-item href="#">FA</b-dropdown-item>
        </b-nav-item-dropdown>

        <b-nav-item href="#" right>Funds</b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
         <!-- <router-view></router-view> -->
 </div>
</template>

<script>

</script>

<style lang="scss" scoped>
 .navbar {
   background-color: #ebf3f3;
 }
</style>
