<template>
  <div id="home">
    <div class="vx-row">
      <div class="vx-col w-full md:w-1/2 mb-base">
        <vx-card>
          <div
            class="vx-row flex-col-reverse md:flex-col-reverse sm:flex-row lg:flex-row"
          >
            <!-- LEFT COL -->
            <div
              class="vx-col w-full md:w-full sm:w-1/2 lg:w-1/2 xl:w-1/2 flex flex-col justify-between"
              v-if="salesBarSession.analyticsData"
            >
              <div>
                <h2 class="mb-1 font-bold">
                  {{ happinessIndicator.series[0] }} %
                </h2>
                <span class="font-medium">Current Happiness</span>

                <!-- Previous Data Comparison -->
                <p class="mt-2 text-xl font-medium">
                  <span
                    :class="
                      (happinessLine.series[0].data[happinessLine.series[0].data.length - 1]- happinessLine.series[0].data[happinessLine.series[0].data.length - 8]) / happinessLine.series[0].data[happinessLine.series[0].data.length - 1]
                        ? 'text-success'
                        : 'text-danger'
                    "
                  >
                    <span
                      v-if="(happinessLine.series[0].data[happinessLine.series[0].data.length - 1]- happinessLine.series[0].data[happinessLine.series[0].data.length - 8]) / happinessLine.series[0].data[happinessLine.series[0].data.length - 1] > 0"
                      >+</span
                    >
                    <span>{{
                      Math.round((happinessLine.series[0].data[happinessLine.series[0].data.length - 1]- happinessLine.series[0].data[happinessLine.series[0].data.length - 8]) / happinessLine.series[0].data[happinessLine.series[0].data.length - 1] * 100)
                    }} %</span>
                  </span>
                  <span> vs </span>
                  <span>{{
                    salesBarSession.analyticsData.comparison.str
                  }}</span>
                </p>
              </div>
              <vs-button
                icon-pack="feather"
                icon="icon-chevrons-right"
                icon-after
                class="shadow-md w-full lg:mt-0 mt-4"
                >View Details</vs-button
              >
            </div>

            <!-- RIGHT COL -->
            <div
              class="vx-col w-full md:w-full sm:w-1/2 lg:w-1/2 xl:w-1/2 flex flex-col lg:mb-0 md:mb-base sm:mb-0 mb-base"
            >
              <vue-apex-charts
                type="radialBar"
                height="240"
                :options="analyticsData.goalOverviewRadialBar.chartOptions"
                :series="happinessIndicator.series"
              />
            </div>
          </div>
          <vs-divider class="my-6"></vs-divider>
          <div class="vx-row">
            <div class="vx-col w-1/2 mb-3">
              <p>Sleep: 8,4 hours</p>
              <vs-progress
                class="block mt-1"
                :percent="50"
                color="primary"
              ></vs-progress>
            </div>
            <div class="vx-col w-1/2 mb-3">
              <p>Sport: 28 min</p>
              <vs-progress
                class="block mt-1"
                :percent="60"
                color="warning"
              ></vs-progress>
            </div>
            <div class="vx-col w-1/2 mb-3">
              <p>Water: 5,3 l</p>
              <vs-progress
                class="block mt-1"
                :percent="70"
                color="danger"
              ></vs-progress>
            </div>
            <div class="vx-col w-1/2 mb-3">
              <p>Beer: 0,7</p>
              <vs-progress
                class="block mt-1"
                :percent="90"
                color="success"
              ></vs-progress>
            </div>
          </div>
        </vx-card>
      </div>
      <div class="vx-col w-full md:w-1/2 mb-base">
        <vx-card title="Happiness">
          <template slot="actions">
            <feather-icon
              icon="SettingsIcon"
              svgClasses="w-6 h-6 text-grey"
            ></feather-icon>
          </template>
          <div slot="no-body" class="p-6 pb-0">
            <vue-apex-charts
              type="line"
              height="288"
              :options="happinessLine.chartOptions"
              :series="happinessLine.series"
            />
          </div>
        </vx-card>
      </div>
    </div>
    <div class="vx-row">
      <!-- OVERLAY CARD 2 -->
      <div class="vx-col w-full lg:w-1/4 sm:w-1/2 mb-base">
        <vx-card class="overlay-card overflow-hidden">
          <template slot="no-body">
            <img
              :src="card_sleep.overlay_img"
              alt="user-profile-cover"
              class="responsive blur-1"
            />
            <div class="card-overlay text-white">
              <div class="flex flex-col justify-between h-full">
                <div class="text-center mt-8 w-full">
                  <h3 class="text-white mb-2 tracking-wide">
                    {{ card_sleep.weather }}
                  </h3>
                  <p class="mb-6">{{ card_sleep.place_name }}</p>
                  <div class="flex justify-around">
                    <feather-icon
                      :icon="card_sleep.weather_icon"
                      svgClasses="w-24 h-24 text-white"
                    />
                    <h2 class="text-white text-big">
                      {{ card_sleep.value }}
                    </h2>
                  </div>
                </div>
                <div class="text-center w-full">
                  <div
                    class="flex justify-between px-8 mb-8 text-xl"
                    v-for="meta in card_sleep.meta"
                    :key="meta.label"
                  >
                    <span>{{ meta.label }}</span>
                    <span>{{ meta.value }}</span>
                  </div>
                </div>
              </div>
            </div>
          </template>
        </vx-card>
      </div>
      <!-- OVERLAY CARD 2 -->
      <div class="vx-col w-full lg:w-1/4 sm:w-1/2 mb-base">
        <vx-card class="overlay-card overflow-hidden">
          <template slot="no-body">
            <img
              :src="card_sport.overlay_img"
              alt="user-profile-cover"
              class="responsive blur-1"
            />
            <div class="card-overlay text-white">
              <div class="flex flex-col justify-between h-full">
                <div class="text-center mt-8 w-full">
                  <h3 class="text-white mb-2 tracking-wide">
                    {{ card_sport.weather }}
                  </h3>
                  <p class="mb-6">{{ card_sport.place_name }}</p>
                  <div class="flex justify-around">
                    <feather-icon
                      :icon="card_sport.weather_icon"
                      svgClasses="w-24 h-24 text-white"
                    />
                    <h2 class="text-white text-big">
                      {{ card_sport.value }}
                    </h2>
                  </div>
                </div>
                <div class="text-center w-full">
                  <div
                    class="flex justify-between px-8 mb-8 text-xl"
                    v-for="meta in card_sport.meta"
                    :key="meta.label"
                  >
                    <span>{{ meta.label }}</span>
                    <span>{{ meta.value }}</span>
                  </div>
                </div>
              </div>
            </div>
          </template>
        </vx-card>
      </div>
      <!-- OVERLAY CARD 2 -->
      <div class="vx-col w-full lg:w-1/4 sm:w-1/2 mb-base">
        <vx-card class="overlay-card overflow-hidden">
          <template slot="no-body">
            <img
              :src="card_water.overlay_img"
              alt="user-profile-cover"
              class="responsive blur-1"
            />
            <div class="card-overlay text-white">
              <div class="flex flex-col justify-between h-full">
                <div class="text-center mt-8 w-full">
                  <h3 class="text-white mb-2 tracking-wide">
                    {{ card_water.weather }}
                  </h3>
                  <p class="mb-6">{{ card_water.place_name }}</p>
                  <div class="flex justify-around">
                    <feather-icon
                      :icon="card_water.weather_icon"
                      svgClasses="w-24 h-24 text-white"
                    />
                    <h2 class="text-white text-big">
                      {{ card_water.value }}
                    </h2>
                  </div>
                </div>
                <div class="text-center w-full">
                  <div
                    class="flex justify-between px-8 mb-8 text-xl"
                    v-for="meta in card_water.meta"
                    :key="meta.label"
                  >
                    <span>{{ meta.label }}</span>
                    <span>{{ meta.value }}</span>
                  </div>
                </div>
              </div>
            </div>
          </template>
        </vx-card>
      </div>
      <!-- OVERLAY CARD 2 -->
      <div class="vx-col w-full lg:w-1/4 sm:w-1/2 mb-base">
        <vx-card class="overlay-card overflow-hidden">
          <template slot="no-body">
            <img
              :src="card_beer.overlay_img"
              alt="user-profile-cover"
              class="responsive blur-1"
            />
            <div class="card-overlay text-white">
              <div class="flex flex-col justify-between h-full">
                <div class="text-center mt-8 w-full">
                  <h3 class="text-white mb-2 tracking-wide">
                    {{ card_beer.weather }}
                  </h3>
                  <p class="mb-6">{{ card_beer.place_name }}</p>
                  <div class="flex justify-around">
                    <feather-icon
                      :icon="card_beer.weather_icon"
                      svgClasses="w-24 h-24 text-white"
                    />
                    <h2 class="text-white text-big">
                      {{ card_beer.value }}
                    </h2>
                  </div>
                </div>
                <div class="text-center w-full">
                  <div
                    class="flex justify-between px-8 mb-8 text-xl"
                    v-for="meta in card_beer.meta"
                    :key="meta.label"
                  >
                    <span>{{ meta.label }}</span>
                    <span>{{ meta.value }}</span>
                  </div>
                </div>
              </div>
            </div>
          </template>
        </vx-card>
      </div>
    </div>
  </div>
</template>

<script>
import VueApexCharts from "vue-apexcharts";
import StatisticsCardLine from "@/components/statistics-cards/StatisticsCardLine.vue";
import analyticsData from "./ui-elements/card/analyticsData.js";
import ChangeTimeDurationDropdown from "@/components/ChangeTimeDurationDropdown.vue";
import VxTimeline from "@/components/timeline/VxTimeline";

export default {
  data() {
    return {
      checkpointReward: {},
      subscribersGained: {},
      ordersRecevied: {},
      salesBarSession: {},
      supportTracker: {},

      happinessIndicator: {
        series: [77.0]
      },

      happinessLine: {
        series: [{
            name: "Happiness",
            data: [
              81.56562868821574,
              75.72474335070547,
              75.19544347602593,
              63.64654147717887,
              75.2441227414171,
              65.19837264568936,
              80.35824557041292,
              48.03904531389341,
              75.53776529394942,
              74.6382871209229,
              71.93412890790476,
              71.20247965104016,
              49.05405399336503,
              50.49885370578157,
              82.01853373346106,
              61.337467372503,
              75.62935032132668,
              64.7895430117315,
              68.4596468597936,
              67.5761388407161,
              82.88897463813916,
              66.91782513494547,
              67.80231415742352,
              75.65690956785771,
              81.09585993769471,
              76.4703730760026,
              74.05676450277025,
              61.46693109328328,
              75.7005970473614,
              77.45952143421712,
            ],
        }],
      chartOptions: {
        chart: {
          toolbar: { show: false },
          dropShadow: {
            enabled: true,
            top: 20,
            left: 2,
            blur: 6,
            opacity: 0.20
          }
        },
        stroke: {
          curve: 'smooth',
          width: 4
        },
        grid: {
          borderColor: '#ebebeb'
        },
        legend: {
          show: false
        },
        colors: ['#df87f2'],
        fill: {
          type: 'gradient',
          gradient: {
            shade: 'dark',
            inverseColors: false,
            gradientToColors: ['#7367F0'],
            shadeIntensity: 1,
            type: 'horizontal',
            opacityFrom: 1,
            opacityTo: 1,
            stops: [0, 100, 100, 100]
          }
        },
        markers: {
          size: 0,
          hover: {
            size: 5
          }
        },
        xaxis: {
          labels: {
            style: {
              cssClass: 'text-grey fill-current'
            }
          },
          axisTicks: {
            show: false
          },
          // categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
          axisBorder: {
            show: false
          }
        },
        yaxis: {
          tickAmount: 5,
          labels: {
            style: {
              cssClass: 'text-grey fill-current'
            },
            formatter (val) {
              return val > 999 ? `${(val / 1000).toFixed(1)}k` : val
            }
          }
        },
        tooltip: {
          x: { show: false }
        },
      },
      },
      productsOrder: {},
      salesRadar: {},
      card_sleep: {
        overlay_img: require('@/assets/images/vladislav-muslakov-CwIU33KGToc-unsplash.jpg'),
        weather: 'Sleep',
        weather_icon: 'MoonIcon',
        value: 0,
        meta: [
          {
            label: 'current',
            value: '8,4 hours'
          },
          {
            label: 'Impact',
            value: '0%'
          },
        ]
      },
      card_sport: {
        overlay_img: require('@/assets/images/clique-images-hSB2HmJYaTo-unsplash.jpg'),
        weather: 'Sport',
        weather_icon: 'ActivityIcon',
        value: '+ 30 min',
        meta: [
          {
            label: 'current',
            value: '28 min'
          },
          {
            label: 'Impact',
            value: '5-10%'
          },
        ]
      },
      card_water: {
        overlay_img: require('@/assets/images/damir-spanic-gzdspwIypvw-unsplash.jpg'),
        weather: 'Water',
        weather_icon: 'DropletIcon',
        value: 0,
        meta: [
          {
            label: 'current',
            value: '5,3 l'
          },
          {
            label: 'Impact',
            value: '0%'
          },
        ]
      },
      card_beer: {
        overlay_img: require('@/assets/images/gerrie-van-der-walt-2uSnxq3M4GE-unsplash.jpg'),
        weather: 'Beer',
        weather_icon: 'GiftIcon',
        value: '+ 0,5 l',
        meta: [
          {
            label: 'current',
            value: '0,7 l'
          },
          {
            label: 'Impact',
            value: '7%'
          },
        ]
      },

      timelineData: [
        {
          color: "primary",
          icon: "PlusIcon",
          title: "Client Meeting",
          desc: "Bonbon macaroon jelly beans gummi bears jelly lollipop apple",
          time: "25 mins Ago",
        },
        {
          color: "warning",
          icon: "MailIcon",
          title: "Email Newsletter",
          desc: "Cupcake gummi bears soufflé caramels candy",
          time: "15 Days Ago",
        },
        {
          color: "danger",
          icon: "UsersIcon",
          title: "Plan Webinar",
          desc: "Candy ice cream cake. Halvah gummi bears",
          time: "20 days ago",
        },
        {
          color: "success",
          icon: "LayoutIcon",
          title: "Launch Website",
          desc:
            "Candy ice cream cake. Halvah gummi bears Cupcake gummi bears soufflé caramels candy.",
          time: "25 days ago",
        },
        {
          color: "primary",
          icon: "TvIcon",
          title: "Marketing",
          desc: "Candy ice cream cake. Halvah gummi bears Cupcake gummi bears.",
          time: "28 days ago",
        },
      ],

      analyticsData,
      dispatchedOrders: [],
    };
  },
  components: {
    VueApexCharts,
    StatisticsCardLine,
    ChangeTimeDurationDropdown,
    VxTimeline,
  },
  created() {
    //  User Reward Card
    this.$http
      .get("/api/user/checkpoint-reward")
      .then((response) => {
        this.checkpointReward = response.data;
      })
      .catch((error) => {
        console.log(error);
      });

    // Subscribers gained - Statistics
    this.$http
      .get("/api/card/card-statistics/subscribers")
      .then((response) => {
        this.subscribersGained = response.data;
      })
      .catch((error) => {
        console.log(error);
      });

    // Orders - Statistics
    this.$http
      .get("/api/card/card-statistics/orders")
      .then((response) => {
        this.ordersRecevied = response.data;
      })
      .catch((error) => {
        console.log(error);
      });

    // Sales bar - Analytics
    this.$http
      .get("/api/card/card-analytics/sales/bar")
      .then((response) => {
        this.salesBarSession = response.data;
      })
      .catch((error) => {
        console.log(error);
      });

    // Sales line
    this.$http
      .get("/api/card/card-analytics/sales/line")
      .then((response) => {
        this.salesLine = response.data;
      })
      .catch((error) => {
        console.log(error);
      });

    // Support Tracker
    this.$http
      .get("/api/card/card-analytics/support-tracker")
      .then((response) => {
        this.supportTracker = response.data;
      })
      .catch((error) => {
        console.log(error);
      });

    // Products Order
    this.$http
      .get("/api/card/card-analytics/products-orders")
      .then((response) => {
        this.productsOrder = response.data;
      })
      .catch((error) => {
        console.log(error);
      });

    // Sales Radar
    this.$http
      .get("/api/card/card-analytics/sales/radar")
      .then((response) => {
        this.salesRadar = response.data;
      })
      .catch((error) => {
        console.log(error);
      });

    // Dispatched Orders
    this.$http
      .get("/api/table/dispatched-orders")
      .then((response) => {
        this.dispatchedOrders = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>

<style lang="scss">
/*! rtl:begin:ignore */
#home {
  .greet-user {
    position: relative;

    .decore-left {
      position: absolute;
      left: 0;
      top: 0;
    }
    .decore-right {
      position: absolute;
      right: 0;
      top: 0;
    }
  }

  @media (max-width: 576px) {
    .decore-left,
    .decore-right {
      width: 140px;
    }
  }
}
/*! rtl:end:ignore */
</style>

