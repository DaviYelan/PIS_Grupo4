document.addEventListener('DOMContentLoaded', function() {
    const notifications = [
        'Notificación 1: Evento importante',
        'Notificación 2: Recordatorio de examen',
        'Notificación 3: Nueva calificación publicada'
    ];

    const notificationContainer = document.querySelector('.notifications');

    notifications.forEach(notification => {
        const notificationItem = document.createElement('div');
        notificationItem.className = 'notification-item';
        notificationItem.textContent = notification;
        notificationContainer.appendChild(notificationItem);
    });
});
