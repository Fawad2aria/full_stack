const mybtn = document.getElementById('submit')
const input = document.getElementById('myinput')

mybtn.onclick = function () {
  var li = document.createElement('li')
  li.innerText = input.value
  document.body.appendChild(li)


  const remBtn = document.createElement('button')
  remBtn.innerText = 'Remove'
  li.appendChild(remBtn)
  
  remBtn.onclick = function () {
    document.body.removeChild(li);
  }
  
  
  const completeBtn = document.createElement('button')
  completeBtn.innerText = 'Complete'
  li.appendChild(completeBtn)

  const completeUl= document.getElementById('mycompleted')
  completeBtn.onclick = function () {

    document.body.removeChild(li);
    completeUl.appendChild(li);
    li.removeChild(completeBtn)
    li.removeChild(remBtn)
     
    const completeRemove = document.createElement('button')
    completeRemove.innerText = 'Remove'
    li.appendChild(completeRemove)

    completeRemove.onclick = function () {
    completeUl.removeChild(li);
     
    }
  }
}
