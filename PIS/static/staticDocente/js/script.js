const body = document.querySelector('body'),
      sidebar = body.querySelector('nav'),
      toggle = body.querySelector(".toggle"),
      searchBtn = body.querySelector(".search-box"),
      modeSwitch = body.querySelector(".toggle-switch"),
      modeText = body.querySelector(".mode-text");

// Elimina la clase 'close' del sidebar cuando la página se carga
document.addEventListener("DOMContentLoaded", () => {
    sidebar.classList.remove("close");
});

toggle.addEventListener("click" , () =>{
    sidebar.classList.toggle("close");
});

searchBtn.addEventListener("click" , () =>{
    sidebar.classList.remove("close");
});

modeSwitch.addEventListener("click" , () =>{
    body.classList.toggle("dark");
    
    if(body.classList.contains("dark")){
        modeText.innerText = "Light mode";
    }else{
        modeText.innerText = "Dark mode";
    }
});
