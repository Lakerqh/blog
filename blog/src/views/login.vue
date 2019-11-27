<template>
  <div id="login" class="common">
    <div class="box">
      <el-input placeholder="username" v-model="username">
        <el-button slot="prepend" icon="el-icon-s-custom"></el-button>
      </el-input>
      <el-input placeholder="password" v-model="username">
        <el-button slot="prepend" icon="el-icon-key"></el-button>
      </el-input>
      <el-button type="primary" icon="el-icon-right"></el-button>
    </div>
  </div>
</template>
<script>
  export default {
    data() {
      return {
        username: '',
      }
    }
  }

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
    background: #709acc;
  }

  .box {
    border: 1px solid #cccccc;
    width: 100%;
    height: 28%;
    background: #e0edf5;
    padding: 0 calc(50% - 300px);
    box-sizing: border-box;
    display: flex;
    justify-content: space-around;
    align-items: center;
  }

</style>
