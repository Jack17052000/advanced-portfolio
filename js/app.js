// Toggle Dark Mode
document.getElementById("theme-toggle").addEventListener("click", () => {
  document.body.classList.toggle("dark");
  document.getElementById("theme-toggle").textContent =
    document.body.classList.contains("dark") ? "☀️" : "🌙";
});

// Contact form
document.getElementById("contact-form").addEventListener("submit", function(e) {
  e.preventDefault();
  alert("¡Gracias por tu mensaje! Te responderé pronto.");
  this.reset();
});
