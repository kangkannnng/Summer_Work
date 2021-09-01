<!--这部分做对比相似代码功能-->
<template>
  <div id="compare">
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
            :default-openeds="['2']"
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
          <el-breadcrumb separator="/">
            <el-breadcrumb-item :to="{ path: '/' }">
              首页
            </el-breadcrumb-item>
            <el-breadcrumb-item>
              对比相似代码
            </el-breadcrumb-item>
            <el-breadcrumb-item>
              请选择两个代码
            </el-breadcrumb-item>
          </el-breadcrumb>
        </el-header>

        <!--这部分开始实现主体功能-->
        <el-main>
          <!--调用数据库内全部数据，使用预测式输入-->
          <div>
            <el-row class="demo-autocomplete">
              <el-col :span="12">
                <div class="sub-title" >
                  请选择第一个文件
                </div>
                <el-autocomplete
                    class="inline-input"
                    v-model="all_file_one"
                    :fetch-suggestions="querySearch_one"
                    placeholder="请选择文件"
                    @select="handleSelect_one"
                ></el-autocomplete>
              </el-col>

              <el-col :span="12">
                <div class="sub-title">
                  请选择第二个文件
                </div>
                <el-autocomplete
                    class="inline-input"
                    v-model="all_file_two"
                    :fetch-suggestions="querySearch_two"
                    placeholder="请选择文件"
                    @select="handleSelect_two"
                ></el-autocomplete>
              </el-col>
            </el-row>
          </div>

          <!--此函数用于修改两个code_area的内容-->
          <div style="margin: 20px 0;">
            <el-button
                type="primary"
                v-on:click="compare_two_file"
            >进行对比
            </el-button>
          </div>

          <!--这部分是代码展示区域-->
          <el-row :gutter="20">
            <el-col :span="12">
                <div class="grid-content bg-purple">
                  <el-input
                      type="textarea"
                      :autosize="{ minRows: 20, maxRows: 100}"
                      placeholder="请输入内容"
                      v-model="code_area1">
                  </el-input>
              </div>
            </el-col>

            <el-col :span="12">
              <div class="grid-content bg-purple">
                <el-input
                    type="textarea"
                    :autosize="{ minRows: 20, maxRows: 100}"
                    placeholder="请输入内容"
                    v-model="code_area2">
                </el-input>
              </div>
            </el-col>
          </el-row>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
export default {
  name: 'compare',
  data() {
    return {
      //最后用于展示代码
      code_area1: '',
      code_area2: '',
      //这个用于输入预测
      file_one: [],
      file_two: [],
      //这个是输入时绑定的模型
      all_file_one: '',
      all_file_two: '',
    }
  },
  methods: {
    //用于修改两个code_area的内容，还没完成
    compare_two_file: function () {
      for(let i = 0; i < this.file_one.length; i++){
        if(this.file_one[i].fields.name === this.all_file_one)
            this.code_area1 = this.file_one[i].fields.code
      }
      for(let i = 0; i < this.file_two.length; i++){
        if(this.file_two[i].fields.name === this.all_file_two)
          this.code_area2 = this.file_two[i].fields.code
      }
      console.log("请看效果！")
    },

    //用于预测
    querySearch_one(queryString, cb) {
      let file_name = [];
      if(queryString) {
        for (let i = 0; i < this.file_one.length; i++) {
          let file = {id: i, value: ""};
          file.value = String(this.file_one[i].fields.name);
          file_name.push(file);
        }
      }
      // 调用 callback 返回建议列表的数据
      cb(file_name);
    },

    querySearch_two(queryString, cb) {
      let file_name = [];
      if(queryString) {
        for (let i = 0; i < this.file_two.length; i++) {
          let file = {id: i, value: ""};
          file.value = String(this.file_two[i].fields.name);
          file.value = String(this.file_two[i].fields.name);
          file_name.push(file);
        }
      }
      // 调用 callback 返回建议列表的数据
      cb(file_name);
    },


    //这个还是要改成axios,还需要返回高亮具体行数
    loadAll() {
      console.log("准备调用数据库全部数据")
      this.$axios.get("/api/load/")
        .then(response =>{
          console.log("返回load数据成功")
          this.all_file_one= JSON.parse(response.data.data)
          this.all_file_two= JSON.parse(response.data.data)
          //立刻添入files数组中
          for (let i = 0; i < this.all_file_one.length && i < this.all_file_two.length; i++){
            this.file_one.push(this.all_file_one[i]);
            this.file_two.push(this.all_file_two[i]);
          }
          console.log("后台数据已成功保存到files中")
        });
    },

    //点击第一个时触发
    handleSelect_one() {
      console.log("已选择第一个文件")
    },

    //点击第二个时触发
    handleSelect_two() {
      console.log("已选择第二个文件")
    },
  },

  mounted() {
    this.loadAll();
  },
}
</script>

<style scoped>
.el-header {
  background-color: #B3C0D1;
  color: #333;
  line-height: 60px;
}

.el-aside {
  color: #333;
}
.el-dropdown-link {
  cursor: pointer;
  color: #409EFF;
}
.el-icon-arrow-down {
  font-size: 12px;
}
.el-dropdown {
  vertical-align: top;
}
.el-dropdown + .el-dropdown {
  margin-left: 30%;
}
.el-icon-arrow-down {
  font-size: 12px;
}
.sub-title {
  height: 30px;
  font-size: larger;
}
</style>

