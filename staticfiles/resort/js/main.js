const burger = document.getElementById('burger');
const menu = document.getElementById('menu');

if (burger && menu) {
  burger.addEventListener('click', () => {
    menu.classList.toggle('active');
  });
}

const revealItems = document.querySelectorAll('.reveal');
if (revealItems.length) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
      }
    });
  }, { threshold: 0.2 });

  revealItems.forEach((item) => observer.observe(item));
}



document.addEventListener("DOMContentLoaded", function () {

  const phoneInput = document.getElementById("id_phone");

  if (phoneInput) {

    phoneInput.addEventListener("focus", function () {
      if (!this.value.startsWith("+996")) {
        this.value = "+996 ";
      }
    });

    phoneInput.addEventListener("input", function () {
      let numbers = this.value.replace(/\D/g, "");

      if (!numbers.startsWith("996")) {
        numbers = "996";
      }

      numbers = numbers.substring(0, 12);

      let formatted = "+996";

      if (numbers.length > 3) {
        formatted += " " + numbers.substring(3, 6);
      }
      if (numbers.length > 6) {
        formatted += " " + numbers.substring(6, 9);
      }
      if (numbers.length > 9) {
        formatted += " " + numbers.substring(9, 12);
      }

      this.value = formatted;
    });

  }

});