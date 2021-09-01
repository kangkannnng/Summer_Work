<!--这部分做匹配相似代码功能-->
<template>
  <div id="check">
    <!--网页的第一个部分：头部-->
    <el-container style="height: auto">
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
      style="height: auto;
        border: 1px solid #eeeeee">
      <!--网页的第二个部分：侧栏-->
      <el-aside
        width="200px"
        style="background-color: rgb(238, 241, 246)">
        <el-menu
            :default-openeds="['1']"
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
          class="el-breadcrumb"
          height="20px"
          style="background-color: #EBEEF5">
          <el-breadcrumb separator="/">
            <el-breadcrumb-item :to="{ path: '/' }">
              首页
            </el-breadcrumb-item>
            <el-breadcrumb-item>
              查看相似代码
            </el-breadcrumb-item>
            <el-breadcrumb-item>
              请选择一个代码
            </el-breadcrumb-item>
          </el-breadcrumb>
        </el-header>

        <!--这部分开始实现主体功能-->
        <el-main>
          <!--调用数据库内全部数据-->
          <el-header style="background-color: #FFFFFF">
              <el-col>
                <div>
                  请选择文件
                </div>
                <!--TODO:这个地方还是不知道为什么默认有对象输入-->
                <el-autocomplete
                  style="width: 350px; padding: 20px"
                  v-model="all_file"
                  :fetch-suggestions="querySearch"
                  placeholder="请输入内容"
                  @select="handleSelect">
                </el-autocomplete>
              </el-col>
          </el-header>

          <el-main>
            <!--此处提供选择展示行数的功能，默认是查看最相似的代码-->
            <div>
              <div style="height: 40px">
                请选择要展示的行数：
                <el-radio
                  v-model="radio"
                  v-bind:label="1">
                  1项
                </el-radio>
                <el-radio
                  v-model="radio"
                  v-bind:label="3">
                  3项
                </el-radio>
                <el-radio
                  v-model="radio"
                  v-bind:label="5">
                  5项
                </el-radio>
              </div>
            </div>

            <!--执行数据处理-->
            <div style="height: 100px">
              <el-row>
                <el-button
                  type="primary"
                  v-on:click="process()">
                  进行匹配
                </el-button>
              </el-row>
            </div>

            <!--这里展示文件基本信息并且可通过点击显示按钮展示具体代码-->
            <template>
              <el-table
                :data="tabledata"
                stripe
                style="width: 100%">
                <el-table-column
                  label="序号"
                  width="200">
                  <template slot-scope="scope">
                    <span style="margin-left: 10px">
                      {{ scope.row.id }}
                    </span>
                  </template>
                </el-table-column>

                <el-table-column
                    label="最相似代码名"
                    width="700">
                  <template slot-scope="scope">
                    <span style="margin-left: 10px">
                      {{ scope.row.name }}
                    </span>
                  </template>
                </el-table-column>

                <el-table-column
                    label="更多操作"
                    width="200">
                  <template slot-scope="scope">
                    <el-button
                      size="mini"
                      @click="see(scope.row.code)"
                      align="left">
                      查看代码
                    </el-button>
                  </template>
                </el-table-column>

                <el-table-column type="expand">
                  <template>
                    <el-form
                      inline
                      class="demo-table-expand">
                      <el-input
                        type="textarea"
                        style="width: 100%"
                        :autosize="{ minRows: 3, maxRows: 4}"
                        placeholder="代码应在此处显示"
                        v-model="codearea">
                      </el-input>
                    </el-form>
                  </template>
                </el-table-column>
              </el-table>
            </template>
          </el-main>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
export default {
  name: 'check',
  data() {
    return {
      //这个用于输入预测
      files: [],
      //这个是输入时绑定的模型
      all_file: '',
      //用于保存输入的id号,待测试，可用于传输要比较的id号
      file_id: '',
      //这个表示单选框默认补选中，测试阶段可以忽略
      radio: 1,
      //用于展示具体代码
      codearea: '',
      //这个用来存储返回的数据，应包含id、文件名和路径
      tabledata: [],
    }
  },

  methods: {

    //核心功能，输入id，返回相似代码类,对接api/test
    process: function () {
      console.log("即将调用test_similar函数")
      //上传id参数
      this.$axios.post("/api/test/", {
        id: this.file_id
      })
        .then((response) => {
          console.log("数据返回成功");
          console.log(response.data.data);
          this.tabledata.push(response.data.data);
          console.log(this.tabledata);
        })
        .catch((error) => {
          console.log(error);
        });
    },


    see: function (str) {
      console.log("准备展示代码！");
      this.codearea = str;
    },

    // 实现输入框的预测功能
    // el-autocomplete元素要求数组内是对象，且有value属性，
    // 由此，此处需要做一个格式调整
    querySearch(queryString, cb) {
      let file_name = [];
      if(queryString) {
        for (let i = 0; i < this.files.length; i++) {
          let file = {id: i, value: ""};
          file.value = String(this.files[i].fields.name);
          file_name.push(file);
        }
      }
      // 调用 callback 返回建议列表的数据
      console.log(file_name);
      cb(file_name);
    },

    // 这个要改为实现获取后端返回的id,文件名和路径
    // 保存到本地的tabledata中
    loadAll() {
      console.log("准备调用数据库全部数据")
      this.$axios.get("/api/load/")
        .then(response =>{
          console.log("返回load数据成功")
          this.all_file= JSON.parse(response.data.data)
          //立刻添入files数组中
          for (let i = 0; i < this.all_file.length; i++)
            this.files.push(this.all_file[i]);
          console.log("后台数据已成功保存到files中")
        });
    },

    //用于点击时执行，保存点击的数据,如文件的id
    handleSelect(item) {
      this.file_id = item.id;
      console.log(this.file_id);
    },
  },

  //created()方法会在页面加载完成之前进行调用
  created() {
    console.log("今日定无BUG")
  },

  //mounted()方法在实例化对象后执行
  mounted() {
    this.loadAll();
  },
}
</script>

<!--style有时间再来管吧，主要就是把外面的style收回-->
<style scoped>
  .el-header {
    background-color: #DCDFE6;
    color: #303133;
    line-height: 20px;
    font-size: medium;
  }
  .el-main-background {
    height: 1000px !important;
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
  .el-dropdown {
    vertical-align: top;
  }
  .el-dropdown + .el-dropdown {
    margin-left: 15px;
  }
  .el-icon-arrow-down {
    font-size: 12px;
  }
  .item:hover {
    box-shadow: 0 0 10px rgba(61, 58, 58, 0.4);
  }
  .datasets-file {
    position: relative;
    width: 880px;
    padding: 15px;
    margin: 40px auto 0;
    font-size: 12px;
    box-shadow: 0 0 10px rgba(233, 169, 169, 0.4);
  }
  .datasets-file .item {
    height: 40px;
    overflow: auto;
    overflow-x: hidden;
    text-align: left;
  }
  .datasets-file > ul {
    list-style: none;
    margin: 0;
    padding: 0
  }
  .dataset-file {
    position: relative;
    height: 52px;
    line-height: 49px;
    overflow: hidden;
    border-bottom: 1px solid #cdcdcd;
  }
</style>

