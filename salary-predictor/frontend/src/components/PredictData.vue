<template>
  <div>
    <div class="predict-data-container">
      <el-input
        class="input"
        placeholder="请输入工作年限"
        v-model.lazy="yearsExperience"
        clearable
        @keypress.enter.native="handleSubmit"
      >
      </el-input>
      <el-button class="button" type="success" @click="handleSubmit"
        >确定</el-button
      >
    </div>
    <div class="predict-result-container">
      <ul v-if="errors && errors.length">
        <li v-for="(error, index) of errors" :key="index">
          {{ error.message }}
        </li>
      </ul>
      <p v-else-if="yearsExperience">预测工资为: {{ predictResult }}</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      yearsExperience: "",
      predictResult: "",
      errors: [],
    };
  },

  methods: {
    handleSubmit() {
      axios
        .post(`${process.env.VUE_APP_API}/salary`, {
          yearsExperience: this.yearsExperience,
        })
        .then((response) => {
          console.log(" response : ", response);
          this.predictResult = response.data.salary.toFixed(2);
        })
        .catch((e) => {
          this.errors.push(e);
        });
    },
  },

  watch: {
    yearsExperience: {
      handler(value) {
        if (value === "") {
          this.predictResult = "";
        }
      },
    },
  },
};
</script>

<style scoped>
.predict-data-container {
  display: flex;
  justify-content: center;
}

.input {
  width: 40vw;
}

.button {
  margin-left: 0.2vw;
}
</style>
