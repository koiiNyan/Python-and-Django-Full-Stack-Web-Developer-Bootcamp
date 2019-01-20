// Object
var carInfo = {
  mark: "Toyota",
  year: 1990,
  model: "Camry",
  carAlert: function(){
    alert("We've got a car here!")
  },
};

// Logging mark to console
console.log(carInfo["mark"]);

// Inside of the function inside of the obj we need to use this to reference the var
// inside the obj. If you don't use this than JS will look for a global var
var simple = {
  prop: "Hello",
  myMethod: function(){
    console.log("The myMethod was called!")
  },
};
console.dir(simple);
//Calling a method inside the obj
simple.myMethod();

// Using this.
var myObj = {
  name: "Nastya",
  greet: function(){
    console.log("Hello " + this.name);
  },
};
console.log(myObj.greet());
