let redirectUrl = [
    'https://google.com',
    'https://translate.google.com',
    'https://www.youtube.com',
    'https://github.com',
    'https://app.slack.com',
];

let counter = document.querySelector('#counter');
let count = 5;

let interval = setInterval(function() {
    counter.innerText = count;
    if (count === 0) {
        let pages = Math.floor(Math.random() *redirectUrl.length);
        location = redirectUrl[pages]
    }
    count -=1
    }, 1000)

