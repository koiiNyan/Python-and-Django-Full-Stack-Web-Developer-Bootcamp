// Event Listeners

// Variables
var headerOne = document.querySelector('#one');
var headerTwo = document.querySelector('#two');
var headerThree = document.querySelector('#three');

// Mouse Over
headerOne.addEventListener("mouseover", function(){
  headerOne.textContent = "Mouse Currently Over Me";
  headerOne.style.color = "red";
})

// When mouse comes off changes to the original
headerOne.addEventListener("mouseout", function(){
  headerOne.textContent = "Hover Over Me!";
  headerOne.style.color = "black";
})

// On Clicks
headerTwo.addEventListener("click", function(){
  headerTwo.textContent = "Clicked On";
  headerTwo.style.color = "blue";
})

// Double Click
headerThree.addEventListener("dblclick", function(){
  headerThree.textContent = "I was double clicked";
  headerThree.style.color = "green";
})
