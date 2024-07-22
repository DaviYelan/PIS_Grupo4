// script.js
document.addEventListener('DOMContentLoaded', () => {
    const table = document.getElementById('progresoTabla');

    table.addEventListener('click', (event) => {
        if (event.target.tagName === 'TD' && event.target.cellIndex === 1) {
            const cell = event.target;
            const currentState = cell.textContent.trim();

            switch (currentState) {
                case 'No Iniciada':
                    cell.textContent = 'En Proceso';
                    cell.className = 'en-proceso';
                    break;
                case 'En Proceso':
                    cell.textContent = 'Completada';
                    cell.className = 'completada';
                    break;
                case 'Completada':
                    cell.textContent = 'No Iniciada';
                    cell.className = 'no-iniciada';
                    break;
            }
        } else if (event.target.tagName === 'BUTTON' && event.target.classList.contains('proyeccion-btn')) {
            const url = event.target.dataset.url;
            window.location.href = url;
        }
    });
});
