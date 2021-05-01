const navButton = document.querySelector(".burger-btn");
const navbar =  document.querySelector(".burger-nav");
const logo = document.querySelector(".logo-btn");
const navIcon = document.querySelector(".burger-btn");

navButton.addEventListener("click", () => {
    navbar.classList.toggle("change");
    logo.classList.toggle("logo-gone");
    navIcon.classList.toggle("change-icon");
});
