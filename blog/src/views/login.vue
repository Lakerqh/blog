<template>
    <div id="login" class="common">
        <div class="box">
            <el-input placeholder="username" v-model="username" @keyup.enter.native="submit" autocomplete="new-password">
                <el-button slot="prepend" icon="el-icon-s-custom"></el-button>
            </el-input>
            <el-input placeholder="password" v-model="password" @keyup.enter.native="submit" show-password autocomplete="new-password">
                <el-button slot="prepend" icon="el-icon-key"></el-button>
            </el-input>
            <el-button type="primary" @click="login" v-if="flag">登录</el-button>
            <el-button type="primary" @click="register" v-else>注册</el-button>
            <a class="register" @click="flag = !flag">登录/注册</a>
        </div>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                flag: true,
                username: "",
                password: "",
            };
        },
        methods: {
            login() {
                let params = {
                    username: this.username,
                    password: this.password
                };
                let url = this.$api.login;
                this.$http.post(url, params).then(res => {
                    if (res.data.code == 0) {
                        this.$message.error(res.data.msg);
                    }else if(res.data.code == 2){
                        this.$message(res.data.msg);
                    }else if(res.data.code ==1){
                        this.$router.push({
                            path:'/home'
                        })
                    }
                })
            },
            submit() {
                this.login()
            },
            register(){
               let params = {
                    username: this.username,
                    password: this.password
                };
                let url = this.$api.register;
                this.$http.post(url, params).then(res => {
                    if (res.data.code == 1) {
                        this.$message.success(res.data.msg);
                        this.flag = true
                    }
                })
            }
        }
    };

</script>
<style scoped>
    /* reset elementui */
    .el-input {
        width: 250px;
    }

    #login {
        display: flex;
        justify-content: space-around;
        align-items: center;
        background: #243369;
    }

    .box {
        border: 1px solid #cccccc;
        width: 100%;
        height: 28%;
        background: #e0edf5;
        padding: 0 calc(50% - 340px);
        box-sizing: border-box;
        display: flex;
        justify-content: space-around;
        align-items: center;
    }

    .register {
        margin-top: 19px;
        font-size: 12px;
        color: #3366ee;
        cursor: pointer;
        user-select: none;
    }

</style>
