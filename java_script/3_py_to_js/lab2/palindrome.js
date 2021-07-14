let first_word = prompt("Enter you first word: ");
let second_word = prompt("Enter your second word: ");

function palindrome(first_word, second_word) {
    var first_word = first_word.split('').sort().join();
    // return first;
    console.log(first_word)
    // var second_word = second_word.replace(' ', '');
    var second_word = second_word.toLowerCase().split('').sort().join();
    console.log(second_word)
    if (first_word === second_word){
        return true;
    }
  
   return false;
}
alert(palindrome(first_word, second_word))