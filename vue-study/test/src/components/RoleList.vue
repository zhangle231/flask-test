
<template>

  <div>

     <van-sticky>

      <van-nav-bar
          title="角色"
          left-arrow
          fixed 
          @click-left="onClickLeft"
      />

      <van-row style="padding:25px"></van-row>

     </van-sticky>
      <van-row>
         <van-col span="4">
            <van-button style="margin-top:10px" 
              size="small" type="primary">添加</van-button>
         </van-col>
         <van-col span="20">
             <van-search 
               v-model="search" show-action @search="onSearch"
               placeholder="3"/>
         </van-col>
      </van-row>
  
     <van-cell-group>
     <van-cell 
	v-for="role in rolelist" :key="role" 
	to="/schemalist" is-link 
	:title="'role' + role" />
     </van-cell-group>
  </div>

</template>

<script>

        export default {
		data: function() {
			return {
				rolelist: [
                                  1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16
                                ],
				search:''
			}
		},
                methods: {
                        onClickLeft() {
                                this.$router.push({path:'/userlist'});
                        },
			onSearch() {
				this.rolelist = [1,2];	
			}
                }
        }

</script>

<style>
</style>
