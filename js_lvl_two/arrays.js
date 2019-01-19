var countries = ["USA", "Germany", "China"];
// counties[0] = "USA"
console.log(countries);

// Reassigning the element of a string
countries[2] = "France";
console.log(countries);

// Array length
len = countries.length;
console.log(len);

var numsArr = ["one", "two", "three"];
console.log(numsArr);
// Removes LAST item from an array
var lastItem = numsArr.pop()
console.log("Item removed: "+numsArr);
// Adds item
numsArr.push("new_item");
console.log("Item added: "+numsArr);

// Last item from the array
var lastItemArr = numsArr[numsArr.length - 1];
console.log("Last Item from the array: "+lastItemArr);

// Nested array
var matrix = [[1,2,3], [4,5,6], [7,8,9]];

////////////////////////////////////////////////////////
// ARRAY ITTERATION
var arr = ["A", "B", "C"];
for(var i=0; i<arr.length; i++){
  console.log(arr[i]);
};

for (letter of arr){
  console.log(letter);
};

// Alert for each element of the array
arr.forEach(alert);

function addAwesome(name) {
  console.log(name+ " is awesome!")
}
addAwesome("django");
var topics = ["python", "django", "science"];
topics.forEach(addAwesome);
