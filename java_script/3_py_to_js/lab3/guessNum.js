
var secretNum = Math.floor(Math.random() * 10);
let correct = false;
while (!correct) {
	guess = prompt('guess a number between 1 to 10: ');
	if (guess == secretNum) {
		correct = true;
		console.log('Right');
	}

	else if (guess < secretNum) {
		console.log('you are low');
	}

	else if (guess > secretNum) {
		console.log('you are higher');
	}
}
