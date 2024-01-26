document.addEventListener('DOMContentLoaded', function () {
    const toggleBtn = document.getElementById('navbarToggleBtn');
    const navbarLinks = document.getElementById('navbarLinks');

    toggleBtn.addEventListener('click', function () {
        navbarLinks.classList.toggle('show');
    });
});