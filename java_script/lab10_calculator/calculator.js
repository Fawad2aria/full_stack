const Calculator = {
  data() {
    return {
      myText: '',
      myPrevous: null,
      myOperator: null,
      operaterClicked: false,
    }
  },
  methods: {
    append (number) {
      if (this.operaterClicked) {
        this.clear();
        this.operaterClicked = false;
      }
      this.myText += number;
    },

    clear () {
      this.myText = '';
    },

    divid () {
      // this.equal()
      this.myOperator = (a,b) => a / b
      this.myPrevous = this.myText
      operaterClicked = true;

    },

    negative () {
      // this.equal()
      this.myOperator = (a,b) => a - b
      this.myPrevous = this.myText
      operaterClicked = true;

    },

    plus () {
      // this.equal()
      this.myOperator = (a,b) => a + b
      this.myPrevous = this.myText
      operaterClicked = true;

    },

    times () {
      // this.equal()
      this.myOperator = (a,b) => a * b
      this.myPrevous = this.myText
      operaterClicked = true;

    },
    equal (){

      if (this.myOperator) {
        this.myText = this.myOperator(Number(this.myPrevous), Number(this.myText))
        this.myOperator = null;
      }
    }
  }



}
const app = Vue.createApp(Calculator);
app.mount('#myCalculator')