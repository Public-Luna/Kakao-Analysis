<template>
  <div id="sample5" :style="style">
    <ScatterChart :chartData="datacollection" :width="width" :height="height" margin="0"/>
  </div>
</template>
<style lang="scss" scoped>
  * {
    margin: 0 auto;
    padding: 0;
  }
  #sample5 {
    margin: 0;
    display: inline-block;
  }
</style>
<script>
import ScatterChart from '@/components/Chart/ScatterChart'

export default {
  name: 'Sample5',
  components: {
    ScatterChart
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
        labels: ['a','b','c','d','e'],
        datasets: [
          {
            label: '홍길동',
            backgroundColor: '#be000044',
            borderColor: '#be0000aa',
            borderWidth: 1,
            data: this.randomPos(5)
          },
          {
            label: '엄준식',
            backgroundColor: '#e4890044',
            borderColor: '#e48900aa',
            borderWidth: 1,
            data: this.randomPos(5)
          },
          {
            label: '고길동',
            backgroundColor: '#9ede7344',
            borderColor: '#9ede73aa',
            borderWidth: 1,
            data: this.randomPos(5)
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
    },
    randomPos(n) {
      var k = []
      for(var i=0;i<n;i++){
        k.push({x: Math.random()*1000, y: Math.random()*1000})
      }
      return k
    }
  },
}
</script>