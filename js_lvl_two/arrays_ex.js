// PART 4 ARRAY EXERCISE

// Creating Empty Student Roster Array
var roster = []

// Create the functions for the tasks

// ADD A NEW STUDENT
// Adds a student to the roster
function addStudent(){
  var name = prompt("Name to add:")
  roster.push(name);
}

// REMOVE STUDENT
// Removes a particular student from the roster, based on his index
function removeStudent(){
  var name = prompt("Name to remove:")
  var index = roster.indexOf(name);
  roster.splice(index,1);
}

// DISPLAY ROSTER
// Prints out the roster to the console.
function display(){
  console.log(roster);
}

////////////////////////////////////////////////////////////////
// Beginning of everything
// Asks user if he wants to use an app
var check = prompt("Would you like to use a roster app? (y/n)")
while (check === 'y'){
    var action = prompt("What would you like to do? (add, remove, display, quit)");
    if (action === 'add'){
      addStudent();
    }
    if (action === 'remove'){
      removeStudent();
    }
    if (action === 'display'){
      display();
    }
    if (action === 'quit'){
      alert("Thanks for using our app!");
      break;
    }
  }
