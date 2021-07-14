let xs = [1, 3, 4, 6, 7, 9];
alert(xs)
let x = prompt("What number do you want to find? ")

function binary_search(xs, x) {
	let min = 0;
	let max = xs.length-1;
	while (min <= max){
        const average = Math.floor((min+max)/2);
        if (xs[average] == x) {
            return average;
        }
        
        else if (xs[average] < x) {
            min = average + 1;
        
        }

        else {
            max = average -1;
        }
   
    
    }
    return 'not existed';
}
alert(binary_search(xs, x))