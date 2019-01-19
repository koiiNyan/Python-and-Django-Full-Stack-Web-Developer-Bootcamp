// Prompting for an answer
var firstName = prompt("Enter your First Name.");
var lastName = prompt("Enter your Second Name.");
var age = prompt("Enter your age please.");
var height = prompt("Enter your height please.");
var pet = prompt("Enter your pet's name.");
//Alerting
alert("Thank you for the information! Check the concole for a detailed answer.");
// Checking conditions for the spy
// Firstly all vars set to false
var nameSpy = false;
var ageSpy = false;
var heightSpy = false;
var petSpy = false;

// The Spy has the same first letter of her First Name and Last Name
if (firstName[0] == lastName[0]){
  nameSpy = true;
};

// The Spy is between the Age of 20 and 30 (exclusive of 20 and 30)
if (20<age && 30>age){
  ageSpy = true;
};

// The Spy is at least 170 centimeters tall.
if(height>=175){
  heightSpy = true;
};

// The Spy has a pet name that ends with the letter "y".
if(pet[pet.length-1] == 'y'){
  petSpy = true;
}

// If everything is fine, log the secret message to console
if(nameSpy && ageSpy && heightSpy && petSpy){
  console.log("I know who you are! Joke ;) You've passed a test.");
} else {
    // else log a smiley.
    console.log("Hello World :^)")
};
