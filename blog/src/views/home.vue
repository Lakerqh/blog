<template>
    <div id="home" class="common">
        <div class="header">
            <h1><img class="logo" src="./../../static/img/logo1.png" alt=""> 图书智能管理系统</h1>
            <div class="setting">
                <span><i class="el-icon-s-custom"></i></span>
                <span><i class="el-icon-s-tools"></i></span>
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
            <!-- <router-view /> -->
            <div v-for="(item,i) in divlist" :key="i" class="test">
                <h3>{{item.name}}</h3>
                <div v-for="(item1,j) in item.children" :key="j">
                    <h4>{{item1.name}}</h4>
                    <span v-for="(item2,k) in item1.children" :key="k" :class="j">{{item.id}}-{{item1.id}}-{{item2.id}}<input name="jack"
                            type="text" :id="item.id+'-'+item1.id+'-'+item2.id"></span>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                list: [0],
                menulist: [],
                id:'',
                divlist: [{
                        name: '大类1',
                        id: 1,
                        children: [{
                                name: '小类1',
                                id: 4,
                                children: [{
                                    name: '参数1',
                                    id: 9,
                                }]
                            },
                            {
                                name: '小类2',
                                id: 16,
                                children: [{
                                        name: '参数1',
                                        id: 10,
                                    },
                                    {
                                        name: '参数2',
                                        id: 11,
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        name: '大类2',
                        id: 2,
                        children: [{
                                name: '小类1',
                                id: 5,
                                children: [{
                                    name: '参数1',
                                    id: 12,
                                }]
                            },
                            {
                                name: '小类2',
                                id: 6,
                                children: [{
                                    name: '参数1',
                                    id: 13,
                                }]
                            },
                            {
                                name: '小类3',
                                id: 7,
                                children: [{
                                    name: '参数1',
                                    id: 14,
                                }]
                            }
                        ]
                    },
                    {
                        name: '大类3',
                        id: 3,
                        children: [{
                            name: '小类1',
                            id: 8,
                            children: [{
                                name: '参数1',
                                id: 15,
                            }]
                        }]
                    }
                ]
            }
        },
        mounted() {
            this.getmenu()
        },
        methods: {
            getval() {
                var dom = document.getElementsByName("jack")
                let Ary = []
                dom.forEach((item, i) => {
                    let id = item.id
                    var idlist = id.split("-");
                    let obj1 = {}
                    let obj2 = {}
                    let obj3 = {}
                    
                    obj1.id = idlist[0]

                    obj2.parentId = idlist[0]
                    obj2.id = idlist[1]

                    obj3.parentId = idlist[1]
                    obj3.id = idlist[2]
                    obj3.name = item.value

                    Ary.push(obj1)
                    Ary.push(obj2)
                    Ary.push(obj3)
                })
                let newAry = []
                let idlist = []
                Ary.forEach(item => {
                    let id = item.id;
                    if(idlist.indexOf(id) == -1){
                        idlist.push(id)
                        newAry.push(item)
                    }
                })
                let result = this.toTree(newAry)
                console.log(result)
            },
            toTree(data) {
                let parents = data.filter(value => value.parentId == 'undefined' || value.parentId == null)
                let children = data.filter(value => value.parentId !== 'undefined' && value.parentId != null)
                let translator = (parents, children) => {
                    parents.forEach((parent) => {
                        children.forEach((current, index) => {
                            if (current.parentId === parent.id) {
                                let temp = JSON.parse(JSON.stringify(children))
                                temp.splice(index, 1)
                                translator([current], temp)
                                typeof parent.children !== 'undefined' ? parent.children.push(
                                    current) : parent.children = [current]
                            }
                        })
                    })
                }

                translator(parents, children)
                return parents
            },
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
                console.log(id)
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
        width: 35px;
        height: 35px;
        border-radius: 30px;
        margin-right: 10px;
    }
    .setting{
        color: #ffffff;
        font-size: 22px;
        margin-right: 20px;
        width: 65px;
        display: flex;
        justify-content: space-between;
    }
    .setting span{
        cursor: pointer;
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
