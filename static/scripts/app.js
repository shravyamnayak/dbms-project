// JavaScript for Hospital Management System

document.addEventListener('DOMContentLoaded', function () {
    // Get the current page URL path
    const path = window.location.pathname;

    // Find the nav link matching the current path and add active class
    const navLinks = document.querySelectorAll('nav ul li a');
    navLinks.forEach(link => {
        if (link.getAttribute('href') === path ||
            (path === '/' && link.getAttribute('href') === '#home')) {
            link.classList.add('active');
        }
    });

    // Appointment date validation - no past dates
    const dateInput = document.getElementById('date');
    if (dateInput) {
        const today = new Date().toISOString().split('T')[0];
        dateInput.setAttribute('min', today);
    }

    // Smooth scroll to sections
    const scrollLinks = document.querySelectorAll('a[href^="#"]');
    scrollLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const id = link.getAttribute('href').substring(1);
            const element = document.getElementById(id);
            if (element) {
                element.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Auto-hide flash messages after 5 seconds
    const flashMessages = document.querySelectorAll('.alert');
    if (flashMessages.length > 0) {
        setTimeout(() => {
            flashMessages.forEach(message => {
                message.style.opacity = '0';
                message.style.transition = 'opacity 1s';
                setTimeout(() => {
                    message.style.display = 'none';
                }, 1000);
            });
        }, 5000);
    }
});