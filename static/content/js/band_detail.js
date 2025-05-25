// static/js/band_detail.js
function animateBandDetail() {
    const photo = document.querySelector('.band-photo');
    const albums = document.querySelector('.albums-container');
    const bandInfo = document.querySelector('.band-info');
    const filterForm = document.querySelector('.search-filter-form');

    // Helper to reset animation
    function resetAnimation(el, className) {
        el.classList.remove(className);
        // Force reflow
        void el.offsetWidth;
        el.classList.add(className);
    }

    if (photo) {
        setTimeout(() => {
            photo.style.opacity = 0;
            photo.style.transform = 'scale(0.7) rotate(-10deg)';
            photo.style.transition = 'none';
            // Force reflow
            void photo.offsetWidth;
            photo.style.transition = 'opacity 0.7s cubic-bezier(.68,-0.55,.27,1.55), transform 0.7s cubic-bezier(.68,-0.55,.27,1.55)';
            photo.style.opacity = 1;
            photo.style.transform = 'scale(1.05) rotate(2deg)';
            setTimeout(() => {
                photo.style.transform = 'scale(1) rotate(0deg)';
            }, 700);
        }, 300);
    }

    if (bandInfo) {
        setTimeout(() => {
            bandInfo.style.opacity = 0;
            bandInfo.style.transform = 'translateX(-60px) skewX(-8deg)';
            bandInfo.style.transition = 'none';
            void bandInfo.offsetWidth;
            bandInfo.style.transition = 'opacity 0.8s cubic-bezier(.68,-0.55,.27,1.55), transform 0.8s cubic-bezier(.68,-0.55,.27,1.55)';
            bandInfo.style.opacity = 1;
            bandInfo.style.transform = 'translateX(0) skewX(0)';
        }, 500);
    }

    if (filterForm) {
        setTimeout(() => {
            filterForm.style.opacity = 0;
            filterForm.style.transform = 'translateY(40px) scale(0.95)';
            filterForm.style.transition = 'none';
            void filterForm.offsetWidth;
            filterForm.style.transition = 'opacity 0.7s cubic-bezier(.68,-0.55,.27,1.55), transform 0.7s cubic-bezier(.68,-0.55,.27,1.55)';
            filterForm.style.opacity = 1;
            filterForm.style.transform = 'translateY(0) scale(1.02)';
            setTimeout(() => {
                filterForm.style.transform = 'translateY(0) scale(1)';
            }, 700);
        }, 900);
    }

    if (albums) {
        setTimeout(() => {
            albums.style.opacity = 0;
            albums.style.transform = 'translateY(60px)';
            albums.style.transition = 'none';
            void albums.offsetWidth;
            albums.style.transition = 'opacity 0.8s cubic-bezier(.68,-0.55,.27,1.55), transform 0.8s cubic-bezier(.68,-0.55,.27,1.55)';
            albums.style.opacity = 1;
            albums.style.transform = 'translateY(0)';
        }, 1200);
    }
}

document.addEventListener("DOMContentLoaded", animateBandDetail);
window.addEventListener('pageshow', function (event) {
    if (event.persisted) {
        animateBandDetail();
    }
});
