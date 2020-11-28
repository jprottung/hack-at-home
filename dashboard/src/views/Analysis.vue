<template>
	<div id="analysis">
    <div class="vx-row">
      <!-- LINE AREA CHART -->
      <div class="vx-col md:w-1/2 w-full mb-base">
          <vx-card title="Sleep level happiness correlation (hours to percent)">
              <vue-apex-charts type="area" height="350" :options="apexChatData.lineAreaChartSplineSleep.chartOptions" :series="apexChatData.lineAreaChartSplineSleep.series"></vue-apex-charts>
          </vx-card>
      </div>
      <div class="vx-col md:w-1/2 w-full mb-base">
          <vx-card title="Sport level happiness correlation (minutes to percent)">
              <vue-apex-charts type="area" height="350" :options="apexChatData.lineAreaChartSplineSport.chartOptions" :series="apexChatData.lineAreaChartSplineSport.series"></vue-apex-charts>
          </vx-card>
      </div>
      <div class="vx-col md:w-1/2 w-full mb-base">
          <vx-card title="Water level happiness correlation (liters to percent)">
              <vue-apex-charts type="area" height="350" :options="apexChatData.lineAreaChartSplineWater.chartOptions" :series="apexChatData.lineAreaChartSplineWater.series"></vue-apex-charts>
          </vx-card>
      </div>
      <div class="vx-col md:w-1/2 w-full mb-base">
          <vx-card title="Beer level happiness correlation (liters to percent)">
              <vue-apex-charts type="area" height="350" :options="apexChatData.lineAreaChartSplineBeer.chartOptions" :series="apexChatData.lineAreaChartSplineBeer.series"></vue-apex-charts>
          </vx-card>
      </div>
    </div>
  </div>
</template>

<script>
import VueApexCharts from 'vue-apexcharts'
import apexChatData from './apexChartData.js'

export default {
  data () {
    return {
      apexChatData
    }
  },
  components: {
    VueApexCharts
  }
}
</script>
