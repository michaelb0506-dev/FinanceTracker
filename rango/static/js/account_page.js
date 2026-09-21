const showMoreBtn = document.getElementById('showMoreBtn');

if (showMoreBtn) {
    showMoreBtn.addEventListener('click', function () {
        document.querySelectorAll('.extra-transaction').forEach(function (el) {
            el.classList.remove('d-none');
        });
        showMoreBtn.classList.add('d-none');
    });
}