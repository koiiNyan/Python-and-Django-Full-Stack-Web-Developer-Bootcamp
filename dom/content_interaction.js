// Choosing paragraph
var p = document.querySelector('p');

// Changing paragraph content. NOTE: changing only TEXT, not html (!)
p.textContent = "Paragraph changed";

// Affecting html and setting paragraph to bold
p.innerHTML = "<strong>I'm bold !</strong>";


// Getting and setting attributes
// Header with id special
var special = document.querySelector('#special');
// Anc tag inside of the header
var specialA = special.querySelector('a');
// Grabbing the link
var l = specialA.getAttribute('href');
// Changing the link
specialA.setAttribute('href', 'https://yandex.ru')
