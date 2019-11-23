import Vue from 'vue';
import Vant from 'vant';
import 'vant/lib/index.css';

import VueRouter from 'vue-router'
import animate from 'animate.css'

import App from './App.vue'
import Test from './Test.vue'
import UserList from './components/UserList.vue'
import RoleList from './components/RoleList.vue'
import SchemaList from './components/SchemaList.vue'

Vue.config.productionTip = false

Vue.use(Vant);
Vue.use(VueRouter)
Vue.use(animate)

const Foo = { 
  template: `
    <div>Foo</div> 
  `
};

const Bar = { 
  template: `
    <div>bar2222222</div> 
  `
};
const User = {
  template: `
    <div>
      <h2>User  {{ $route.params.id }}</h2>
      <router-view></router-view>
    </div>
  `,
  watch:{
    '$route'(to,from){
      console.log(to,from);
    }
  }
}

const UserHome = { template: ' <div> user_home </div>' };
const UserProfile = { template: ' <div> user_profile </div>' };
const UserPosts = { template: ' <div> user_posts </div>' };



const routes = [
  { path: '/userlist', component: UserList},
  { path: '/rolelist', component: RoleList},
  { path: '/schemalist', component: SchemaList},
  { path: '/foo', component: Foo },
  { path: '/bar', component: Bar },
  { path: '/test', component: Test },
  { path: '/user/:id', component: User,
    children:[
      { path: '', component:UserHome },
      { path: 'profile', component:UserProfile },
      { path: 'posts', component:UserPosts},
    ]
  }
]

const router = new VueRouter({
    routes: routes
})


new Vue({
  router,
  render: h => h(App),
}).$mount('#app')

router.push('/user/lixin');
router.push({path:'/userlist'});
