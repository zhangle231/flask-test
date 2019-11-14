<template>
  <div id="app">
    <!--
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    -->
     <h1>Hello App!</h1>
     <p>
       <ul>
         <li>
          <router-link to="/foo">Go to Foo</router-link>
         </li>
         <li>
          <router-link to="/bar">Go to Bar</router-link>
         </li>
         <li>
          <router-link to="/test">Go to Test</router-link>
         </li>
       </ul>
     </p>
     <router-view></router-view>
  </div>
</template>

<script>

//import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'app',
  components: {
    //HelloWorld
  }
}
</script>

<style>
#app1 {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
