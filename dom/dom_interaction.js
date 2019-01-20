// Interacting with the first header
var first = document.querySelector('#first');
// Changing color
first.style.color = 'red';

// Second header
var second = document.querySelector('#second');

// Creating random color generator
function randomColorGen(){
  // String of characters for generating a hex color
  var chars = "0123456789ABCDEF";
  var color = "#";
  // Generating a random color string of 6 hex chars
  for (var i = 0; i<6; i++) {
    color += chars[Math.floor(Math.random() *16)];
  }
  return color
}

// Changing the header color
function changeHC(header){
  randomColor = randomColorGen();
  header.style.color = randomColor;
}

// Setting the action to change color in an interval in millisecs
setInterval("changeHC(second)", 500);
