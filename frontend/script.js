// Select typing text element
const typingText = document.getElementById("typing-text");

typingText.textContent = "Build Your Future";


// Select registration form
const registrationForm = document.getElementById("registration-form");

registrationForm.addEventListener("submit", function(event) {

    event.preventDefault();

    console.log("Registration form submitted");

});