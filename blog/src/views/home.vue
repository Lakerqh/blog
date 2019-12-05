<template>
    <div id="home" class="common">
        <div class="header">
            <h1><img class="logo" src="./../../static/img/login/logo1.png" alt=""> 图书智能管理系统</h1>
            <div class="setting">
                <span>{{usermessage.username}}</span>
                <span @click="signout"><i class="el-icon-s-tools"></i></span>
            </div>
        </div>
        <div class="slider">
            <div class="box" v-for="(item,i) in menulist" :key="i">
                <h1 @click="packup(i)">
                    <span><i class="el-icon-s-order"></i>{{item.name}}</span>
                    <i class="el-icon-caret-bottom" v-if="list.indexOf(i) != -1"></i><i class="el-icon-caret-right" v-else></i>
                </h1>
                <h2 @click="selectNav(item1.id)" :class="{active:item1.id == id}" v-for="(item1,j) in item.children" :key="j" v-show="list.indexOf(i) != -1">{{item1.name}}</h2>
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
                usermessage: JSON.parse(localStorage.getItem('usermessage')),
                list: [0],
                menulist: [],
                id:'',
            }
        },
        mounted() {
            this.getmenu()
        },
        methods: {
            getmenu() {
                let url = this.$api.getmenu;
                this.$http.get(url).then(res => {
                    this.menulist = res.data.list
                })
            },
            packup(i) {
                let index = this.list.indexOf(i);
                if (index == -1) {
                    this.list.push(i)
                } else {
                    this.list.splice(index, 1)
                }
            },
            selectNav(id){
                this.id = id
            },
            signout(){
                this.$router.push({
                    path:'/login'
                })
            }
        }
    }

</script>
<style scoped>
    .header {
        height: 60px;
        background: #2083d8;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .header h1{
        font-size: 17px;
        color: #ffffff;
        font-weight: normal;
        display: flex;
        align-items: center;
        margin-left: 20px;
    }
    .logo{
        width: 70px;
        height: 70px;
    }
    .setting{
        color: #ffffff;
        font-size: 22px;
        margin-right: 20px;
        display: flex;
        justify-content: space-between;
    }
    .setting span{
        cursor: pointer;
        margin-left: 15px;
    }

    .slider {
        float: left;
        height: calc(100% - 60px);
        width: 230px;
        background: #ffffff;
        overflow: auto;
    }

    .slider h1,
    .slider h2 {
        margin: 0;
        padding: 0;
        color: #222222;
        font-weight: normal;
        height: 40px;
        cursor: default;
    }

    .slider h1 {
        font-size: 16px;
        box-sizing: border-box;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0 20px 0 35px;
        user-select: none;
    }
    .el-icon-s-order{
        margin-right: 8px;
        color: #2083d8;
    }

    .slider h2 {
        color: #525566;
        font-size: 13px;
        box-sizing: border-box;
        display: flex;
        justify-content: flex-start;
        align-items: center;
        padding: 0 20px 0 60px;
    }
    .active{
        background: #2083d8;
        color: #ffffff !important;
        font-weight: bold;
    }

    .section {
        margin-left: 230px;
        height: calc(100% - 60px);
        background: #f2f2f2;
        box-sizing: border-box;
        overflow: auto;
    }

    .test {
        border: 1px solid #333333;
    }

</style>
