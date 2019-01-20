// Restart Game Button var
var restart = document.querySelector("#button");

// All the squares on the board
var squares = document.querySelectorAll("td");


// Function to clear everything
function clearBoard() {
  // Changing every cell to an empty string
  for (var i = 0; i < squares.length; i++) {
      squares[i].textContent = '';
  }

}

// Listen for click on a restart button
restart.addEventListener("click",clearBoard)



// Function to change the square marker
function changeMarker(){
    if(this.textContent === ''){
      this.textContent = 'X';
    }else if (this.textContent === 'X') {
      this.textContent = 'O';
    }else {
      this.textContent = '';
    }
};

// Use a for loop to add Event listeners to all the squares
for (var i = 0; i < squares.length; i++) {
    // Change a marker on a click
    squares[i].addEventListener("click", changeMarker);
}
