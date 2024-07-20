const body = document.querySelector('body'),
      sidebar = body.querySelector('nav'),
      toggle = body.querySelector(".toggle"),
      searchBtn = body.querySelector(".search-box"),
      modeSwitch = body.querySelector(".toggle-switch"),
      modeText = body.querySelector(".mode-text");

// Verificar el estado del modo oscuro al cargar la página
document.addEventListener("DOMContentLoaded", () => {
    if (localStorage.getItem('darkMode') === 'enabled') {
        body.classList.add('dark');
        modeText.innerText = "Light mode";
    } else {
        modeText.innerText = "Dark mode";
    }
});

toggle.addEventListener("click", () => {
    sidebar.classList.toggle("close");
});

searchBtn.addEventListener("click", () => {
    sidebar.classList.remove("close");
});

modeSwitch.addEventListener("click", () => {
    body.classList.toggle("dark");
    
    if (body.classList.contains("dark")) {
        modeText.innerText = "Light mode";
        localStorage.setItem('darkMode', 'enabled');
    } else {
        modeText.innerText = "Dark mode";
        localStorage.setItem('darkMode', 'disabled');
    }
});
