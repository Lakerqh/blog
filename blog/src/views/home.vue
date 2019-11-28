<template>
    <div id="home" class="common">
        <div class="header">
            ss
        </div>
        <div class="slider">
            <div class="box" v-for="(item,i) in menulist" :key="i">
                <h1 @click="packup(i)"><span>{{item.name}}</span><i class="el-icon-caret-bottom" v-if="list.indexOf(i) != -1"></i><i class="el-icon-caret-right" v-else></i></h1>
                <h2 v-for="(item1,j) in item.children" :key="j" v-show="list.indexOf(i) != -1">{{item1.name}}</h2>
            </div>
        </div>
        <div class="section">
            <router-view />
        </div>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                list:[0],
                menulist: [],
            }
        },
        mounted(){
            this.getmenu()
        },
        methods: {
            getmenu() {
                let url = this.$api.getmenu;
                this.$http.get(url).then(res => {
                   this.menulist = res.data.list
                })
            },
            packup(i){
                let index = this.list.indexOf(i);
                if(index == -1){
                    this.list.push(i)
                }else{
                    this.list.splice(index,1)
                }
            }
        }
    }

</script>
<style scoped>
.header{
    height: 60px;
    background: #ffffff;
}
.slider{
    float: left;
    height: calc(100% - 60px);
    width: 230px;
    background: #243352;
}
h1, h2{
    margin: 0;
    padding: 0;
    color: #ffffff;
    font-weight: normal;
    height: 40px;
    border-bottom: 1px solid #243369;
}
h1{
    font-size: 17px;
    font-family: 'Courier New', Courier, monospace;
    box-sizing: border-box;
    display: flex;
    justify-content:space-between;
    align-items: center;
    padding: 0 20px;
}
h2{
    color: #cccccc;
    font-size: 13px;
    box-sizing: border-box;
    display: flex;
    justify-content:flex-start;
    align-items: center;
    padding: 0 20px;
}
.section{
    margin-left: 230px;
    height: calc(100% - 60px);
    background: #f2f2f2;
    box-sizing: border-box;
    overflow: auto;
}
</style>
