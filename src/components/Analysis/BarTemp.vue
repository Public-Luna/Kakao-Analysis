<template>
  <div id="sample2" :style="style">
    <BarChart :chartData="datacollection" :width="width" :height="height" margin="0"/>
  </div>
</template>
<style lang="scss" scoped>
  * {
    margin: 0 auto;
    padding: 0;
  }
  #sample2 {
    margin: 0;
    display: inline-block;
  }
</style>
<script>
import BarChart from '@/components/Chart/BarChart'

export default {
  name: 'Sample2',
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
      datacollection: null,
      loaded: false,
    }
  },
  mounted() {
    this.fillData()
  },
  computed: {
    style() {
      return {
        width: this.width + 'px',
        height: this.height + 'px',
      }
    }
  },
  methods: {
    fillData() {
      this.datacollection = {
        labels: ['2020.01','2020.02','2020.03','2020.04'],
        datasets: [
          {
            label: '비속어 사용',
            backgroundColor: '#f8ede3',
            borderColor: '#798777',
            pointBackgroundColor: '#798777',
            borderWidth: 1,
            pointBorderColor: '#bdd2b6',
            data: this.randomList(4)
          },
        ]
      }
    },
    randomList(n) {
      /* 우우우우 나영채 리듬게임 짱 못한다 */
      var k = []
      for(var i=0;i<n;i++){
        k.push(Math.random()*1000)
      }
      return k
    }
  },
}
</script>