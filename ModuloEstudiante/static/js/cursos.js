document.addEventListener('DOMContentLoaded', function() {
    const courses = [
        'Curso 1: Introducción a la Programación',
        'Curso 2: Matemáticas Avanzadas',
        'Curso 3: Física Experimental'
    ];

    const courseContainer = document.querySelector('.courses');

    courses.forEach(course => {
        const courseItem = document.createElement('div');
        courseItem.className = 'course-item';
        courseItem.textContent = course;
        courseContainer.appendChild(courseItem);
    });
});
