const Quotes = {
    data() {
        return {
            quotes: [],
            newQuote: '', 
            page: 1                   
        }
        
    },
    methods: {
        GetQuotes () {
        // let page = 1
        fetch(`https://favqs.com/api/quotes?page=${this.page}&filter=${this.newQuote}`, {
            headers: {
                Authorization: `Token token="4aef2fbe90991a51f78c33970e2790a3"`
            }
        }).then(res=> res.json())
        .then(data => {
            this.quotes = data.quotes
            console.log(this.quotes)
        }) 
        this.page ++
    }
    }
}
const app = Vue.createApp(Quotes);
app.mount('#myQuotes')