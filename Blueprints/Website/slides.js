const num_slides = 19;
const slides = Array.from({length: num_slides}, (_, i) => `slides/slide_${i + 1}.jpg`);
let currentSlide = 0;

const slideElement = document.querySelector('.slide img');
const prevButton = document.querySelector('.prev-button');
const nextButton = document.querySelector('.next-button');

function loadImage(img, src) {
    img.src = src;
    img.removeAttribute('data-src');
}

function updateSlide() {
    loadImage(slideElement, slides[currentSlide]);
    prevButton.disabled = currentSlide === 0;
    nextButton.disabled = currentSlide === slides.length - 1;
}

function nextSlide() {
    if (currentSlide < slides.length - 1) {
        currentSlide++;
        updateSlide();
    }
}

function prevSlide() {
    if (currentSlide > 0) {
        currentSlide--;
        updateSlide();
    }
}

prevButton.addEventListener('click', prevSlide);
nextButton.addEventListener('click', nextSlide);

// Initial setup
updateSlide();
