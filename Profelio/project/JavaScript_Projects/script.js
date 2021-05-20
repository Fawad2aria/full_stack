const calculator = {
    data() {
        return {
            myText: 0,
            myPreviewsText: null,
            myOperator: null,
            OperatorClicked: false,
        }
    }, 
    methods: {
        clear() {
            this.myText = '';
        },

        module () {
            this.myText = parseFloat(this.myText)/100;
        },

        decimal () {
            if (!this.myText.includes('.')){
                this.appendNumber('.');
            }
        },

        appendNumber (number) {
            if (this.OperatorClicked) {
                this.clear();
                this.OperatorClicked = false;
            }
            this.myText += number;

        },
        
        negate () {
            if (!this.myText.includes('-')) {
                this.myText = `-${this.myText}`
            }
            
            else {
                this.myText 
                
            }
        },
        divid () {
        
            this.myOperator = function(a,b){
                return b/a;
            }
            this.myPreviewsText = this.myText;
            this.OperatorClicked = true;
        },
        times () {
        
            this.myOperator = (a, b) => b * a;
            this.myPreviewsText = this.myText;
            this.OperatorClicked = true;
        },
        subtract () {
        
            this.myOperator = (a, b) => b - a;
            this.myPreviewsText = this.myText;
            this.OperatorClicked = true;
        },
        plus () {
        
            this.myOperator = (a, b) => b + a;
            this.myPreviewsText = this.myText;
            this.OperatorClicked = true;
        },
        equal () {
            this.myText = `${this.myOperator(
                parseFloat(this.myText),
                parseFloat(this.myPreviewsText)
            )}`;
            this.myPreviewsText = null;
        }


    }    
}
Vue.createApp(calculator).mount('#myCalculator')