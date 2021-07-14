console.log('hello world');
// if statement//
let temperature = 56;
if (temperature < 60) {
    alert('cold');
} else if (temperature < 80) {
    alert('warm');
} else {
    alert('hot');
}
//------------------------------------------------------------------------

//while loop//
let i = 0;
while (i < 10) {
    console.log(i);
    i++;
}


let invalidInput = true;
while (invalidInput) {
    answer = prompt("Pick a number from one to ten");
    if (answer >= 1 && answer <= 10) {
        invalidInput = false;
    }
}
//-----------------------------------------------------------------------------------
// for loop//

/*
fruits = ['apple', 'banana', 'cherry']

for fruit in fruits:
    print(fruit)
*/

let fruits = ['apple', 'banana', 'cherry'];

fruits.forEach(function(fruit) {
    console.log(fruit);
});



let fruits = ['apple', 'bananana', 'pear'];
fruits.push('cherry');
for (let i=0; i<fruits.length; i++) {
    console.log(fruits[i]);
}
console.log(fruits.indexOf('bananana')); // 1
//-------------------------------------------------------------------------
// functions//

function add(a, b) {
    return a + b;
}
console.log(add(5, 2));


var add = function(a, b) {
    return a + b;
}; // this is a statement, and needs a semi-colon
console.log(add(5, 2));
//----------------------------------------------------------------------------

// Dictionary //

let library_user = {
    first_name: 'Jane',
    last_name: 'Smith',
    age: 20,
    books: [{
        title: 'A Wrinkle in Time',
        author: 'Madeleine L\'Engle',
        published: 1962
    },{
        title: 'The Giving Tree',
        author: 'Shel Silverstein',
        published: 1964
    }]
};

console.log(library_user.first_name); // Mike
console.log(library_user[first_name]); // Mike
console.log(library_user.books[0].title); // A Wrinkle in Time
console.log(library_user[books][0][title]); // A Wrinkle in Time
//--------------------------------------------------------------------------
// Modules

let calculations = {
    add: function(a, b) {
        return a + b;
    },
    subtract: function(a, b) {
        return a - b;
    },
    multiply: function(a, b) {
        return a * b;
    },
    divide: function(a, b) {
        return a / b;
    }
};

calculations.add(10, 5); // 11
calculations.subtract(10, 5); // 5
calculations.multiply(10, 5); // 50
calculations.divide(10, 5); // 2

//---------------------------------------------------------------------------------------
// classes

class ATM {
    constructor(balance=0) {
      this.balance = balance;
    }
    get_balance() {
      return this.balance;
    }
}

let atm = new ATM(5.0);
alert(atm.get_balance());

//---------------------------------------------------------------------
// Inheritance 
class Animal {
    constructor(legs = 0) {
        this.legs = legs;
    }

    move() {
        if (this.legs > 0) {
            console.log('walk');
        } else {
            console.log('slither');
        }
    }
}

class Dog extends Animal {
    constructor(legs = 4, sound = 'ruff') {
        super(legs); // invoke the parent class's constructor
        this.sound = sound;
    }

    bark() {
        console.log(this.sound);
    }
    
    move() { // override the parent method
      super.move(); // call the parent method (optional)
      console.log('dog moving');
    }
}

let myDog = new Dog(4);

console.log(myDog.legs); // logs 4
myDog.move(); // logs 'walk', 'dog moving'
myDog.bark(); // logs 'ruff
class Animal {
    constructor(legs = 0) {
        this.legs = legs;
    }

    move() {
        if (this.legs > 0) {
            console.log('walk');
        } else {
            console.log('slither');
        }
    }
}

class Dog extends Animal {
    constructor(legs = 4, sound = 'ruff') {
        super(legs); // invoke the parent class's constructor
        this.sound = sound;
    }

    bark() {
        console.log(this.sound);
    }
    
    move() { // override the parent method
      super.move(); // call the parent method (optional)
      console.log('dog moving');
    }
}

let myDog = new Dog(4);

console.log(myDog.legs); // logs 4
myDog.move(); // logs 'walk', 'dog moving'
myDog.bark(); // logs 'ruff
//---------------------------------------------------------------
// Object prototypes

function Animal(legs) {
    this.legs = legs || 0; // use default value if needed
}

Animal.prototype.move = function () {
    if (this.legs > 0) {
        console.log('walk');
    } else {
        console.log('slither');
    }
};

function Dog(legs, sound) {
    Animal.call(this, legs); // parent 'constructor'
    this.sound = sound || 'ruff';
}

Dog.prototype = Object.create(Animal.prototype);

Dog.prototype.bark = function () {
    console.log(this.sound);
};

var myDog = new Dog(4);

console.log(myDog.legs); // logs 4
myDog.move(); // logs 'walk'
myDog.bark(); // logs 'ruff'
