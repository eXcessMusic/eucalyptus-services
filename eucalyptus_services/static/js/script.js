

const burgerButton = document.querySelector('.burger');
const menuLinks = document.getElementById("myLinks");

burgerButton.addEventListener('click', displayMenu);

/* Toggle between showing and hiding the navigation menu links when the user clicks on the hamburger menu / bar icon */
function displayMenu() {
  var x = document.getElementById("myLinks");
  if (x.style.opacity === "1") {
    x.style.opacity = "0"; // Hide the menu with fade effect
    setTimeout(function() {
      x.style.display = "none"; // Hide the menu after fading out
      burgerButton.classList.remove('cross'); // Remove the 'cross' class to revert the animation
    }, 100); // Adjust the duration of the fade effect (in milliseconds)
  } else {
    x.style.display = "block"; // Show the menu immediately
    setTimeout(function() {
      x.style.opacity = "1"; // Fade in the menu gradually
    }, 10); // Add a slight delay before fading in for the effect
    burgerButton.classList.add('cross'); // Add the 'cross' class to trigger the animation
  }
}
