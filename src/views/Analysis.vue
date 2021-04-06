
<template>
  <div class="small">
    <Chart :chart-data='datacollection'></Chart>
    <button @click="fillData()">Randomize</button>
  </div>
</template>

<script>
  import Chart from '@/components/Chart.js'

  export default {
    components: {
      Chart
    },
    data() {
      return {
        datacollection: null,
        loaded: false
      }
    },
    methods: {
      fillData () {
        this.datacollection = {
          labels: [0,1,2,3,4,5],
          datasets: [
            {
              label: 'Data Two',
              backgroundColor: '#dddddd',
              borderColor: 'lightblue',
              pointBackgroundColor: 'blue',
              borderWidht: 1,
              pointBorderColor: 'blue',
              data: [0,0,1,2,4]
            },
            {
              label: 'Data One',
              backgroundColor: '#f87979',
              borderColor: 'lightblue',
              pointBackgroundColor: 'blue',
              borderWidht: 1,
              pointBorderColor: 'blue',
              data: [0,1,2,3,4,5]
            },
          ]
        }
      },
      getRandomInt () {
        return Math.floor(Math.random() * (50 - 5 + 1)) + 5
      }
    }
  }
</script>

<style>
  .small {
    max-width: 600px;
    margin:  150px auto;
  }
</style>