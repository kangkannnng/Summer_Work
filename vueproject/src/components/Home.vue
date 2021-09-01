<!--欢迎界面-->
<template>
  <div id="home">
    <!--网页的第一个部分：头部-->
    <el-container>
      <el-header
        height="70px"
        style="background-color: #EBEEF5">
        <h1>
          内部版本
        </h1>
      </el-header>
    </el-container>

    <el-container
      style="height: 500px;
        border: 1px solid #eeeeee">
      <!--网页的第二个部分：侧栏-->
      <el-aside
        width="200px"
        style="background-color: rgb(238, 241, 246)">
        <el-menu
            :default-openeds="['1', '2', '3']"
            :default-active="this.$router.path"
            router>
          <!--第一个功能（查看相似代码）-->
          <el-submenu index="1">
            <template slot="title">
              <i class="el-icon-s-tools"></i>
              查看相似代码
            </template>
            <el-menu-item index="/check">
              请选择一个代码
            </el-menu-item>
          </el-submenu>

          <!--第二个功能（对比相似代码）-->
          <el-submenu index="2">
            <template slot="title">
              <i class="el-icon-setting"></i>
              对比相似代码
            </template>
            <el-menu-item index="/compare">
              请选择两个代码
            </el-menu-item>
          </el-submenu>

          <!--第三个功能（查看更多细节）-->
          <el-submenu index="3">
            <template slot="title">
              <i class="el-icon-user-solid">
              </i>
              查看项目细节
            </template>
            <el-menu-item index="/manage">
              查看更多细节
            </el-menu-item>
          </el-submenu>
        </el-menu>
      </el-aside>

      <!--网页的第三个部分：主界面-->
      <el-container>
        <!--这部分为导航-->
        <el-header
          height="20px"
          style="background-color: rgb(238, 241, 246)">
          <el-breadcrumb
            separator="/">
            <el-breadcrumb-item :to="{ path: '/' }">
              首页
            </el-breadcrumb-item>
            <el-breadcrumb-item>
              欢迎
            </el-breadcrumb-item>
          </el-breadcrumb>
        </el-header>

        <!--这部分开始实现具体功能-->
        <el-main>
          <h1>{{ django_message }}</h1>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
export default {
  data(){
    return{
      django_message: "",
    }
  },
  //created()方法会在页面加载完成之前进行调用
  created() {
    this.$axios.get("/api/hello/")
      .then(response => {
        console.log(response.data)
        this.django_message = response.data.message
      })
  }
};
</script>

<style>
.el-header {
  background-color: #B3C0D1;
  color: #333;
  line-height: 60px;
}
.el-aside {
  color: #333;
}
.h1 {
  font-size: larger;
  text-align: center;
}
</style>

