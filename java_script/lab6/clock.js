setInterval(function myTimer() {
    var d = new Date();
    let hrs = d.getHours();
    let mn = d.getMinutes();
    let ss = d.getSeconds();
    let date = d.toLocaleDateString();
    var nowtime = `${date} ${hrs}:${mn}:${ss}`   
    // var nowtime = date+' ' +hrs+':'+mn+':'+ss;
    document.getElementById("myClock").innerHTML = nowtime;
}, 1000) 



let bt = document.querySelector('#myStart')
let date = new Date();
let id;

// lapBtn.style.display ='none';
bt.onclick = function () {
    clearLaps()
    clearInterval(id)
    date.setHours(0,0,0,0);
    bt.innerHTML = formatDate(date);
    id = setInterval(function(){
        let time = date.getTime();
        time += 1000
        date = new Date(time)
        bt.innerHTML = formatDate(date);
    }, 1000)
}

const lapBtn = document.getElementById('lap');
const laps = document.getElementById('laps')

lapBtn.onclick = function () {
    
    const li = document.createElement('li')
    li.innerText = formatDate(date);
    laps.appendChild(li)
}

function formatDate (date){
    function pad (number) {
        if (number <10) {
            return '0' + number
        }
        return number
    }
    const hours = pad(date.getHours())
    const minutes = pad(date.getMinutes())
    const seconds = pad(date.getSeconds())
    return `${hours}:${minutes}:${seconds}`
}
function clearLaps() {
    const lapsLi = document.querySelectorAll('#laps li')
    lapsLi.forEach(li => laps.removeChild(li))
}



