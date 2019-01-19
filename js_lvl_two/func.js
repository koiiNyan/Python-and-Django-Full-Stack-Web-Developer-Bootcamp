function hello(){
  console.log("Hello world!");
}

function helloYou(name){
  console.log("Hello "+name);
}

function addNum(num1, num2) {
  console.log(num1+num2);
}

function helloSmOne(name="Frankie") {
  console.log("Hello "+name);
}

function formal(name="Sam", title="Sir"){
  return title+" "+name;
}
// 'Welcome ' + formal() will print Welcome Sir Sam

function timesFive(numInp) {
  var result = numInp * 5;
  return result;
}
