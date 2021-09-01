<!--这部分展示实习过程中的一些细节-->
<template>
  <div id="manage">
    <!--网页的第一个部分：头部-->
    <el-container>
      <el-header
        class="el-header"
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
        <!--使用菜单来直观展示功能-->
        <el-menu
            :default-openeds="['3']"
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
        <!--这部分为导航部分-->
        <el-header
          class="el-breadcrumb"
          height="20px"
          style="background-color: #E4E7ED">
          <el-breadcrumb separator="/">
            <el-breadcrumb-item :to="{ path: '/' }">
              首页
            </el-breadcrumb-item>
            <el-breadcrumb-item>
              这里是实习过程中的一些细节工作,这个实习有很多收获   : )
            </el-breadcrumb-item>
          </el-breadcrumb>
        </el-header>

        <!--展示图片-->
        <el-main>
          <el-carousel
            :interval="5000"
            type="card"
            height="300px">
            <el-carousel-item
              v-for="url in urls"
              :key="url">
              <h3 class="medium">
                <el-image
                style="width: 480px;
                  height: 300px"
                :src="url"></el-image>
              </h3>
            </el-carousel-item>
          </el-carousel>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
export default {
  name: "manage",
  data(){
    return {
      urls:[
        '/static/assets/design.jpg',
        '/static/assets/django.jpg',
        '/static/assets/english.jpg',
        '/static/assets/paper.jpg',
        '/static/assets/problem.jpg',
        '/static/assets/python_code.jpg'
      ]
    }

  }
};
</script>

<style scoped>
  .el-header {
    background-color: #DCDFE6;
    color: #303133;
    line-height: 20px;
    font-size: medium;
  }
  .el-main-background {
    height: 1000px;
  }
  .el-aside {
    width: 210px !important;
    background-color: #E4E7ED;
  }
  .el-menu {
    width: 208px !important;
    border: 1px solid #E4E7ED;
  }
  .el-breadcrumb {
    height:20px !important;
    background-color: #E4E7ED;
  }
  .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
    background-color: #d3dce6;
  }
  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
</style>

