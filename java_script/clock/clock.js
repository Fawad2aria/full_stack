const Clock = {
    data () {
      return {
        date: new Date(),
        shouldDisplayClock: true
      }
    },
    mounted () {
      setInterval(() => {
        this.date = new Date()
      }, 1000)
    },
    methods: {
      formatDate () {
        const hours = this.date.getHours()
        const minutes = this.date.getMinutes()
        const seconds = this.date.getSeconds()
        return `${hours}:${minutes}:${seconds}`
      },
      displayDate () {
        this.shouldDisplayClock = false
      },
      displayClock () {
        this.shouldDisplayClock = true
      }
    }
  }
  Vue.createApp(Clock).mount('#clock')