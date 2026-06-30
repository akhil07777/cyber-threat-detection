document.addEventListener('DOMContentLoaded', function () {
    var sidebarToggleButtons = document.querySelectorAll('[data-sidebar-toggle]');
    var dashboardSidebar = document.querySelector('.dashboard-sidebar');

    sidebarToggleButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            if (!dashboardSidebar) {
                return;
            }

            var isCollapsed = dashboardSidebar.classList.toggle('is-collapsed');
            button.setAttribute('aria-expanded', String(!isCollapsed));
        });
    });

    var uploadProgress = document.querySelector('.upload-progress .progress-bar');
    var uploadButton = document.querySelector('.upload-btn');

    if (uploadButton && uploadProgress) {
        uploadButton.addEventListener('click', function () {
            uploadProgress.style.width = '72%';
            uploadProgress.parentElement.setAttribute('aria-valuenow', '72');
        });
    }

    var themeToggle = document.querySelector('[data-theme-toggle]');
    if (themeToggle) {
        themeToggle.addEventListener('click', function () {
            document.body.classList.toggle('theme-dark');
            themeToggle.innerHTML = document.body.classList.contains('theme-dark')
                ? '<i class="bi bi-sun me-2"></i>Theme'
                : '<i class="bi bi-moon-stars me-2"></i>Theme';
        });
    }
});
