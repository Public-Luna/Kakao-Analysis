
<template>
  <div id="analysis">
    <router-view></router-view>
    <div>
      <TestAnalysis class="item"/>
    </div>
    <div>
      <LineTemp class="item"/>
      <LineTemp class="item"/>
      <BarTemp class="item"/>
      <BarTemp class="item"/>
    </div>
    <div>
      <PieTemp class="item"/>
      <PieTemp class="item"/>
      <RaderTemp class="item"/>
      <RaderTemp class="item"/>
    </div>
    <div>
      <ScatterTemp class="item"/>
      <ScatterTemp class="item"/>
      <DoughnutTemp class="item" />
      <DoughnutTemp class="item" />
    </div>
    <div>
      <BubbleTemp class="item" />
      <BubbleTemp class="item" />
    </div>
  </div>
</template>

<script>
  import TestAnalysis from '@/components/Analysis/TestAnalysis'
  import LineTemp from '@/components/Analysis/LineTemp'
  import BarTemp from '@/components/Analysis/BarTemp'
  import PieTemp from '@/components/Analysis/PieTemp'
  import RaderTemp from '@/components/Analysis/RadarTemp'
  import ScatterTemp from '@/components/Analysis/ScatterTemp'
  import DoughnutTemp from '@/components/Analysis/DoughnutTemp'
  import BubbleTemp from '@/components/Analysis/BubbleTemp'

  export default {
    name: 'analysis',
    components: {
      TestAnalysis,
      LineTemp,
      BarTemp,
      PieTemp,
      RaderTemp,
      ScatterTemp,
      DoughnutTemp,
      BubbleTemp,
    },
    data() {
      return {

      }
    },
    mounted() {
      
    },
    methods: {
      
    }
  }
</script>

<style lang="scss" scoped>
  #analysis {
    text-align: center;
    .item {
      padding: 20px;
    }
  }
</style>