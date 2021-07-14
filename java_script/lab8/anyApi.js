
const API_KEY = '5839d42b000c958c5002e817d20c51d7'
let mySend = document.getElementById("mySend")
let myUl =document.getElementById('myUl')
let mydiv =document.getElementById('mydiv')
let myArray =document.getElementById('myArray')


mySend.onclick = function() {
    var cityName = document.getElementById('cityName').value;
    // let cityName = 'London'
    let units = 'imperial'
 
    var url = `https://api.openweathermap.org/data/2.5/weather?q=${cityName}&appid=${API_KEY}&units=${units}`
    clearPage()
    fetch(url).then(res => res.json())
    .then(data => {
        
        const names = data.name
        mydiv.innerHTML= names


        const weathers = data.weather
        const lis = weathers.map(weather=> {
            const li = document.createElement('li')
            li.innerText = `Main: ${weather.main}
                Description: ${weather.description}`
            return li
        })
        myArray.appendChild(...lis)


        var datas = data.main
        var li = document.createElement('li')
            li.innerText = `Temp: ${datas.temp}
            Feels_alike: ${datas.feels_like}
            Max_temp: ${datas.temp_max}
            Min_temp: ${datas.temp_min}
            Humidity: ${datas.humidity}
            winds: ${data.wind.speed}
          `
            myUl.appendChild(li)
            
            console.log(data)  
            
        })
        

}
function clearPage() {
    const dataLi = document.querySelectorAll('#myUl li')
    dataLi.forEach(li => myUl.removeChild(li))
}
