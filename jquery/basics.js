// All h1 items
$('h1');

// All li items
$('li');

// Saving to variable
var x = $('h1');

// Adding css
// Text color
x.css('color', 'red');
// Bckground color
x.css('background', 'blue');


// Passing an obj to a var
var newCSS = {
  'color':'white',
  'background':'blue',
  'border':'20px solid red',
};
x.css(newCSS);


// Grabbing multiple objects at once
var listItems = $('li');
// and change everything in the li
listItems.css('color', 'blue');
// Grab a particular index item
listItems.eq(0).css('color', 'orange');
// Last item
listItems.eq(-1).css('color', 'orange');


// Changing text
$('h1').text('Text Changed!');
// Changing HTML
$('h1').html("<em>new</em> text");


///////////////////////////////////
// ATTRIBUTES && CLASSES         //
// Changing second input from button to a checkbox
$('input').eq(1).attr('type', 'checkbox');
// Editting a value
$('input').eq(0).val('new value!');


// ADDING A CLASS
// doesn't overwrite x.css(newCSS)
$('h1').addClass('turnRed');
// remove a class
$('h1').removeClass('turnRed');
// Toggling a class (turning class on/off - don't need to add and remove with
// this)
$('h1').toggleClass('turnBlue');
