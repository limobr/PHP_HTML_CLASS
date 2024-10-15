const colorButton = document.getElementById("colorButton")
colorButton.addEventListener('click', ()=>{
    colorButton.style.backgroundColor=colorButton.style.backgroundColor==='blue' ? '#4caf50': 'blue'
})

function myFunction() {
    document.getElementById("paragraphClick").innerHTML = "Button has already been clicked."
  }