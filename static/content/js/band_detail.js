// static/js/band_detail.js

function animateBandDetail() {
    const photo = document.querySelector('.band-photo');
    const albums = document.querySelector('.albums-container');
    const bandInfo = document.querySelector('.band-info');
    const filterForm = document.querySelector('.search-filter-form');

    if (photo) {
        setTimeout(() => {
            photo.classList.add('animate-zoom');
        }, 300);
    }

    if (bandInfo) {
        setTimeout(() => {
            bandInfo.classList.add('animate-slide-left');
        }, 500);
    }

    if (filterForm) {
        setTimeout(() => {
            filterForm.classList.add('animate-slide-up');
        }, 900);
    }

    if (albums) {
        setTimeout(() => {
            albums.classList.add('animate-slide-up');
        }, 1200);
    }
}

document.addEventListener("DOMContentLoaded", animateBandDetail);
window.addEventListener('pageshow', function (event) {
    if (event.persisted) {
        animateBandDetail();
    }
});
