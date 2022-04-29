<template>
  <div class="data-chart-container">
    <div id="my-chart"></div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {};
  },

  mounted() {
    axios
      .get(`${process.env.VUE_APP_API}/data`)
      .then((response) => {
        const { point, line, coef, intercept } = response.data;
        this.drawGraph(point, line, coef[0], intercept[0]);
      })
      .catch((error) => {
        console.log(error);
      });
  },

  methods: {
    drawGraph(point, line, coef, intercept) {
      const markLineOpt = {
        animation: false,
        label: {
          formatter: `y = ${coef.toFixed(2)} * x + ${intercept.toFixed(2)}`,
          align: "right",
        },
        lineStyle: {
          type: "solid",
          color: "green",
          width: 4,
        },
        tooltip: {
          formatter: `y = ${coef.toFixed(2)} * x + ${intercept.toFixed(2)}`,
        },
        data: [
          [
            {
              coord: line[0],
              symbol: "none",
            },
            {
              coord: line[1],
              symbol: "none",
            },
          ],
        ],
      };
      const option = {
        xAxis: {
            type: "value",
            name: "工作年限",
        },
        yAxis: {
            type: "value",
            name: "收入",
        },
        title: {
          text: "收入&工作年限",
          left: "center",
          top: 0,
        },

        tooltip: {
          formatter: " {a}: ({c})",
        },
        series: [
          {
            name: "坐标",
            symbolSize: 20,
            type: "scatter",
            data: point,
            markLine: markLineOpt,
          },
        ],
      };

      const myChart = this.$echarts.init(document.getElementById("my-chart"));
      myChart.setOption(option);
    },
  },
};
</script>

<style scoped>
.data-chart-container {
  display: flex;
  justify-content: center;
}

#my-chart {
  height: 45vh;
  width: 45vw;
}
</style>
