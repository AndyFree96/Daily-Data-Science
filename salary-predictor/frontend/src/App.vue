<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <data-chart></data-chart>
    <predict-data></predict-data>
  </div>
</template>

<script>
import PredictData from "./components/PredictData.vue"
import DataChart from "./components/DataChart.vue"

export default {
  name: 'App',
  components: {
    PredictData,
    DataChart,
  },
  data () {
    return {
    }
  },
  mounted () {
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
