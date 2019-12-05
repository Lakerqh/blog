<template>
    <div id="login" class="common">
        <div class="box">
            <div class="tabs">
                <span @click="selectTab" :class="{active:flag}">登录</span>
                <span @click="selectTab" :class="{active:!flag}">读者注册</span>
            </div>
            <div class="form" v-show="flag">
                <el-form :model="ruleForm_l" :rules="rules_l" ref="ruleForm_l" label-width="0" class="demo-ruleForm">
                    <el-form-item prop="username">
                        <el-input placeholder="username" v-model="ruleForm_l.username" autocomplete="new-password">
                            <el-button slot="prepend" icon="el-icon-s-custom"></el-button>
                        </el-input>
                    </el-form-item>
                    <el-form-item prop="password">
                        <el-input placeholder="password" v-model="ruleForm_l.password" show-password
                            autocomplete="new-password">
                            <el-button slot="prepend" icon="el-icon-key"></el-button>
                        </el-input>
                    </el-form-item>
                </el-form>
                <div class="footerbtn">
                    <span @click="login('ruleForm_l')">登&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;录</span>
                </div>
            </div>
            <div class="formr" v-show="!flag">
                <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-position="left" label-width="80px"
                    class="demo-ruleForm">
                    <el-form-item label="姓名" prop="username">
                        <el-input v-model="ruleForm.username"></el-input>
                    </el-form-item>
                    <el-form-item label="密码" prop="password">
                        <el-input v-model="ruleForm.password" show-password autocomplete="new-password"></el-input>
                    </el-form-item>
                    <el-form-item label="确认密码" prop="cpassword">
                        <el-input v-model="ruleForm.cpassword" show-password autocomplete="new-password"></el-input>
                    </el-form-item>
                    <el-form-item label="电话" prop="phone">
                        <el-input v-model="ruleForm.phone"></el-input>
                    </el-form-item>
                    <el-form-item label="邮箱" prop="email">
                        <el-input v-model="ruleForm.email"></el-input>
                    </el-form-item>
                    <el-form-item label="性别" prop="gender">
                        <el-radio-group v-model="ruleForm.gender">
                            <el-radio label="1">男</el-radio>
                            <el-radio label="0">女</el-radio>
                        </el-radio-group>
                    </el-form-item>
                </el-form>
                <div class="footerbtn">
                    <span @click="register('ruleForm')">注&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;册</span>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    export default {
        data() {
            return {
                flag: true,
                ruleForm_l: {
                    username: '',
                    password: '',
                },
                rules_l: {
                    username: [{
                        required: true,
                        message: '请输入登录账号',
                        trigger: 'blur'
                    }],
                    password: [{
                        required: true,
                        message: '请输入密码',
                        trigger: 'blur'
                    }]
                },
                ruleForm: {
                    username: '',
                    password: '',
                    cpassword: '',
                    phone: '',
                    email: '',
                    gender: '1',

                },
                rules: {
                    username: [{
                        required: true,
                        message: '请输入姓名',
                        trigger: 'blur'
                    }, ],
                    password: [{
                        required: true,
                        message: '请输入密码',
                        trigger: 'blur'
                    }],
                    cpassword: [{
                        required: true,
                        message: '请再次确认密码',
                        trigger: 'blur'
                    }],
                    phone: [{
                        required: true,
                        message: '请输入电话号码',
                        trigger: 'blur'
                    }],
                    email: [{
                        required: true,
                        message: '请输入邮箱',
                        trigger: 'blur'
                    }, {
                        type: 'email',
                        message: '请输入正确邮箱地址',
                        trigger: 'blur'
                    }],
                    gender: [{
                        required: true,
                        trigger: 'change'
                    }],
                }
            };
        },
        methods: {
            selectTab() {
                this.flag = !this.flag;
            },
            login(formName) {
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        let params = this.ruleForm_l;
                        let url = this.$api.login;
                        this.$http.post(url, params).then(res => {
                            if (res.data.code == 1) {
                                this.$router.push({
                                    path: '/home'
                                })
                                localStorage.setItem('usermessage',JSON.stringify(res.data.usermessage))
                            } else {
                                this.$message.error(res.data.msg);
                            }
                        })
                    } else {
                        console.log('error submit!!');
                        return false;
                    }
                });
            },
            register(formName) {
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        let params = this.ruleForm;
                        let url = this.$api.registeReader;
                        this.$http.post(url, params).then(res => {
                            if (res.data.code == 1) {
                                this.$message.success(res.data.msg);
                                this.$refs[formName].resetFields();
                            }
                        })
                    } else {
                        console.log('error submit!!');
                        return false;
                    }
                });
            }
        }
    };

</script>
<style scoped>
    #login {
        display: flex;
        justify-content: space-around;
        align-items: center;
        background: url('./../../static//img/login/bg.png') no-repeat center;
        background-size: 100% 100%;
    }

    .box {
        border: 1px solid #cccccc;
        width: 500px;
        background: #e0edf5;
    }

    .tabs {
        height: 35px;
        background: #ffffff;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .tabs span {
        width: 50%;
        text-align: center;
        font-size: 14px;
        font-weight: bold;
        cursor: default;
        height: 35px;
        line-height: 35px;
    }

    .active {
        background: #e0edf5;
        color: #3366ee;
    }

    .form {
        padding: 40px 80px 20px 80px;
    }

    .formr {
        padding: 40px 80px 20px 80px;
    }

    .footerbtn {}

    .footerbtn span {
        height: 35px;
        background: #3366ee;
        color: #ffffff;
        font-size: 16px;
        font-weight: bold;
        line-height: 35px;
        text-align: center;
        width: 100%;
        display: inline-block;
        cursor: pointer;
    }

</style>
