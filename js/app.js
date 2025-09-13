// Toggle Dark Mode
const themeBtn = document.getElementById("theme-toggle");
if (themeBtn) {
  themeBtn.addEventListener("click", () => {
    const dark = document.body.classList.toggle("dark");
    themeBtn.textContent = dark ? "☀️" : "🌓";
  });
}

// Contact form (envía al backend FastAPI)
const form = document.getElementById("contact-form");
const msg = document.getElementById("msg");
if (form) {
  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const data = new FormData(form);
    try {
      const res = await fetch("http://127.0.0.1:8000/contacto/", {
        method: "POST",
        body: data,
      });
      const result = await res.json();
      if (msg) msg.textContent = result.msg || "Mensaje enviado.";
      form.reset();
    } catch (error) {
      if (msg) msg.textContent = "Error al enviar, intenta de nuevo.";
      console.error(error);
    }
  });
}

