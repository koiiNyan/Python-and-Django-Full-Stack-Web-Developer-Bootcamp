// Basic event handling with jQuery.
// Clicking action on header1
$('h1').click(function(){
  console.log('There was a click!');
})

$('li').click(function(){
  console.log('Any li was clicked!');
})

// Changing h1 when Clicking
$('h1').click(function(){
  var length = 8,
        charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
        pass = "";
    for (var i = 0, len = charset.length; i < length; ++i) {
        pass += charset.charAt(Math.floor(Math.random() * len));
    }
  $(this).text("Password generator: "+ pass);
})


// KEY PRESS
// Toggling class on and off when inputting text in the first input
$('input').eq(0).keypress(function(event){
  $('h3').toggleClass('turnBlue');
  // event - in obj which: letter pressed
  // we can specify event.which to grab a particular symbol
  console.log(event);
  // 13 - enter key
  // if pressed enter - toggle class to .turnRed
  if (event.which === 13){
    $('h3').toggleClass('turnRed');
  }
})

/////////////////
// on() acts like an event listener
// When double click on a paragraph, toggle .turnRed
$('p').on('dblclick', function(){
  $(this).toggleClass('turnRed');
})

// Mouse Hovering
$('p').on('mouseenter', function(){
  $(this).toggleClass('turnRed');
})


///////////////////////////
// EVENT && ANIMATIONS   //
//
//When clicking on submit button, container fades out. 3000 ms.
$('input').eq(1).on('click', function(){
  $('.container').fadeOut(3000);
})

// Slide Up
$('input').eq(1).on('click', function(){
  $('.container').slideUp(3000);
})
