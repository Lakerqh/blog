<template>
   <div id="user">
       <span @click="check">审核</span>
   </div>
</template>
<script>
   export default{
       data(){
           return {

           }
       },
       methods: {
           check(){
                let params = {
                    id:5
                }
                let url = this.$api.check;
                this.$http.post(url, params).then(res => {
                    
                })
           }
       }
   }
</script>
<style scoped>
   
</style>
