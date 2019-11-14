import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'

Vue.config.productionTip = false

Vue.use(VueRouter)

const Foo = { template: '<div>foo1111111</div>' }
const Bar = { template: '<div>bar2222222</div>' }

const routes = [
  { path: '/foo', component: Foo },
  { path: '/bar', component: Bar }
]

const router = new VueRouter({
    routes: routes
})


new Vue({
  router,
  render: h => h(App),
}).$mount('#app')

