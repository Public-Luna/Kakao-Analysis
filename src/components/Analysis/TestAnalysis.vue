<template>
  <div id="TestAnalysis" :style="style">
    <BarChart :key="updated" :chartData="datacollection" :options="options" :width="width" :height="height" margin="0"/>
  </div>
</template>
<style lang="scss" scoped>
  * {
    margin: 0 auto;
    padding: 0;
  }
  #TestAnalysis {
    margin: 0;
    display: inline-block;
  }
</style>
<script>
import BarChart from '@/components/Chart/BarChart'
import { mapGetters } from "vuex";
import { FETCH_CHART } from '@/store/actions.type'

export default {
  name: 'TestAnalysis',
  components: {
    BarChart
  },
  props: {
    width: {
      Number,
      default: 300
    },
    height: {
      Number,
      default: 300
    },
  },
  data() {
    return {
      updated: 0,
      config: {},
      datacollection: {
        labels: [],
        datasets: [
          {
            label: '비속어 사용',
            backgroundColor: '#f8ede3',
            borderColor: '#798777',
            pointBackgroundColor: '#798777',
            borderWidth: 1,
            pointBorderColor: '#bdd2b6',
            data: []
          },
        ],
      },
      options: {
        scales: {
          yAxes: [{
            ticks: {
              beginAtZero: true
            },
            gridLines: {
              display: true
            }
          }],
          xAxes: [ {
            gridLines: {
              display: false
            }
          }]
        },
        legend: {
          display: true
        },
        responsive: true,
      }
    }
  },
  mounted() {
    this.fetchTest()
  },
  computed: {
    style() {
      return {
        width: this.width + 'px',
        height: this.height + 'px',
      }
    },
    ...mapGetters(["isLoading", "chart"])
  },
  watch: {
    chart (val) {
      this.datacollection.labels = val.labels
      this.datacollection.datasets[0].data = val.data
      this.datacollection.datasets[0].label = val.title
      this.updated ++;
    }
  },
  methods: {
    fetchTest() {
      this.$store.dispatch(FETCH_CHART, this.config);
    },
  },
}
</script>