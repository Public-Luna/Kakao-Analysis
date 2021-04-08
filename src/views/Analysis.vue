
<template>
  <div id="analysis">
    <div>
      <Sample1 class="item"/>
      <Sample1 class="item"/>
      <Sample1 class="item"/>
    </div>
    <div>
      <Sample2 class="item"/>
      <Sample2 class="item"/>
      <Sample2 class="item"/>
    </div>
    <div>
      <Sample3 class="item"/>
      <Sample3 class="item"/>
      <Sample3 class="item"/>
    </div>
    <div>
      <Sample4 class="item"/>
      <Sample4 class="item"/>
      <Sample4 class="item"/>
    </div>
  </div>
</template>

<script>
  import Sample1 from '@/components/Analysis/Sample1'
  import Sample2 from '@/components/Analysis/Sample2'
  import Sample3 from '@/components/Analysis/Sample3'
  import Sample4 from '@/components/Analysis/Sample4'

  export default {
    name: 'analysis',
    components: {
      Sample1,
      Sample2,
      Sample3,
      Sample4
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