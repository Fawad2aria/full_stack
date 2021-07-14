/*
const API_KEY = '4aef2fbe90991a51f78c33970e2790a3'
const filter = 'earth'
const url = `https://favqs.com/api/quotes?page=${1}&filter=${filter}`
fetch(url, {
  headers: {
      Authorization: `Token token="${API_KEY}"`
    }
}).then(res => res.json())
.then(data => {
      const quotes = data.quotes
      

      const lis = quotes.map(quote=> {
          const li = document.createElement('li')
          li.innerText = `Author: ${quote.author}, Text: ${quote.body}`
          return li
        })
        
        document.body.append(...lis)
    })
*/
/*
const API_KEY = '4aef2fbe90991a51f78c33970e2790a3'
const filter = 'earth'
const url = `https://favqs.com/api/quotes?page=${2}&filter=${filter}`
fetch(url, {
  headers: {
    Authorization: `Token token="${API_KEY}"`
  }
}).then(res => res.json())
  .then(data => console.log(data))
*/

const API_KEY = '4aef2fbe90991a51f78c33970e2790a3'
const myClick = document.getElementById('myClick')
var myNext = document.getElementById('myNext')
const myUl = document.getElementById('myUl')
const counter = document.getElementById('counter')
let last_page = false;
let page = 1
let count = 0
myClick.onclick = function(){
    clearPage()
    var filter = document.getElementById('myInput').value;
    filter = encodeURIComponent(filter.trim())
    var url = `https://favqs.com/api/quotes?page=${page}&filter=${filter}`
    fetch(url, {
    headers: {
        Authorization: `Token token="${API_KEY}"`
    }
    }).then(res => res.json())
    .then(renderQuotes)
    
    function renderQuotes (data) {
        const quotes = data.quotes
        console.log(data)
    quotes.forEach(quote => {
        const li = document.createElement('li')
        li.innerText = `Author: ${quote.author}, Text: ${quote.body}`
        myUl.appendChild(li)
    })
}
    myNext.onclick = function() {
        clearPage()
        var filter = document.getElementById('myInput').value;
        page +=1
        var url = `https://favqs.com/api/quotes?page=${page}&filter=${filter}`
        fetch(url, {
            headers: {
                Authorization: `Token token="${API_KEY}"`
            }
        }).then(res => res.json())
        .then(renderQuotes)
        function renderQuotes (data) {
            const quotes = data.quotes
            if (last_page === true){
                function myNext() {
                var myNext = document.getElementById('myNext').disabled = true;
                }
            }
            quotes.forEach(quote => {
                const li = document.createElement('li')
                li.innerText = `Author: ${quote.author}, Text: ${quote.body}`
                myUl.appendChild(li)
            })
        }
        count +=1
        counter.innerText = count
    }
    count +=1
    counter.innerText = count
}

function clearPage() {
    const quotesLi = document.querySelectorAll('#myUl li')
    quotesLi.forEach(li => myUl.removeChild(li))
}
