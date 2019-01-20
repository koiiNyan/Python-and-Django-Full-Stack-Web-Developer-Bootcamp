// Grabbing items
// jQuery
var divs = $('div');
// Vanilla
var divs = document.querySelectorAll('div');

// Editting the style of a certain var
// jQuery
$(element).css('border-width', '20px');
// Vanilla
element.style.borderWidth = '20px';


// Calling function when document obj model is ready
// jQuery
$(document).ready(function(){
  //code here
});

// Vanilla
function ready(fn) {
  if (document.readyState != 'loading'){
    fn();
  } else {
    document.addEventListener('DOMContentLoaded', fn);
  }
};
