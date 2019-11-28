<template>
    <div id="home" class="common">
        <div class="header">
            ss
        </div>
        <div class="slider">
            <div class="box" v-for="(item,i) in menulist" :key="i">
                <h1>{{item.name}}</h1>
                <h2 v-for="(item1,j) in item.children" :key="j">{{item1.name}}</h2>
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
        }
    }

</script>
<style scoped>
.header{
    height: 80px;
    background: #ffffff;
}
.slider{
    float: left;
    height: calc(100% - 80px);
    width: 230px;
    background: #243352;
}
h1, h2{
    margin: 0;
    padding: 0;
    color: #ffffff;
}
h1{
    font-size: 17px;
    font-family: 'Courier New', Courier, monospace;
}
h2{
    font-size: 15px;
}
.section{
    margin-left: 230px;
    height: calc(100% - 80px);
    background: #f2f2f2;
    box-sizing: border-box;
    overflow: auto;
}
</style>
