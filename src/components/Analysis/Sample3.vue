<template>
  <div id="sample3" :style="style">
    <PieChart :chartData="datacollection" :width="width" :height="height" margin="0"/>
  </div>
</template>
<style lang="scss" scoped>
  * {
    margin: 0 auto;
    padding: 0;
  }
  #sample3 {
    margin: 0;
    display: inline-block;
  }
</style>
<script>
import PieChart from '@/components/Chart/PieChart'

export default {
  name: 'Sample3',
  components: {
    PieChart
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
        labels: ['a','b','c','d'],
        datasets: [
          {
            label: '비속어 사용',
            backgroundColor: ['#be0000','#e48900','#f7ea00','#9ede73'],
            borderWidht: 1,
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