const Any_api= {
    data () {
        return {
            results: null,
            source: ''.toUpperCase(),
            currencies: ''.toUpperCase(),
            amount: null,

        }
    },
    methods: {
        get_anyApi () {
            var url = `http://apilayer.net/api/live?access_key=c99ac9ef90c1c5234def6d8a299e272d&currencies=${this.currencies}&source=${this.source}&format=1`
            fetch(url).then(res => res.json())
            .then(data => {
                this.results = data
                console.log(this.results)
            })
            
        },
        mulitiply () {
            this.result = this.amount * 0.83
        }

    },
}
const app = Vue.createApp(Any_api);
app.mount('#myAny_api')
