// Esperar a que el DOM se haya cargado
document.addEventListener("DOMContentLoaded", function() {
    // Datos para los gráficos
    const data1 = {
        labels: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'],
        datasets: [{
            label: 'Calificaciones',
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1,
            data: [65, 59, 80, 81, 56, 55],
        }]
    };

    const data2 = {
        labels: ['Rojo', 'Azul', 'Amarillo', 'Verde', 'Morado', 'Naranja'],
        datasets: [{
            label: 'Colores Favoritos',
            backgroundColor: ['rgba(255, 99, 132, 0.2)', 'rgba(54, 162, 235, 0.2)', 'rgba(255, 206, 86, 0.2)', 'rgba(75, 192, 192, 0.2)', 'rgba(153, 102, 255, 0.2)', 'rgba(255, 159, 64, 0.2)'],
            borderColor: ['rgba(255, 99, 132, 1)', 'rgba(54, 162, 235, 1)', 'rgba(255, 206, 86, 1)', 'rgba(75, 192, 192, 1)', 'rgba(153, 102, 255, 1)', 'rgba(255, 159, 64, 1)'],
            borderWidth: 1,
            data: [12, 19, 3, 5, 2, 3],
        }]
    };

    const data3 = {
        labels: ['A', 'B', 'C', 'D', 'E'],
        datasets: [{
            label: 'Puntajes',
            backgroundColor: 'rgba(153, 102, 255, 0.2)',
            borderColor: 'rgba(153, 102, 255, 1)',
            borderWidth: 1,
            data: [23, 45, 76, 56, 33],
        }]
    };

    // Opciones para los gráficos
    const options = {
        responsive: true,
        maintainAspectRatio: false,
    };

    // Crear gráficos
    const ctx1 = document.getElementById('chart1').getContext('2d');
    new Chart(ctx1, {
        type: 'bar',
        data: data1,
        options: options
    });

    const ctx2 = document.getElementById('chart2').getContext('2d');
    new Chart(ctx2, {
        type: 'pie',
        data: data2,
        options: options
    });

    const ctx3 = document.getElementById('chart3').getContext('2d');
    new Chart(ctx3, {
        type: 'line',
        data: data3,
        options: options
    });
});
