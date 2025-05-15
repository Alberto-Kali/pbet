const slider = document.querySelector('.slider');
const sliderImages = document.querySelectorAll('.inventorys1');
const sliderLine = document.querySelector('.inventory1');
console.log(sliderImages)
let sliderCount = 0;
let sliderWidth = slider.offsetWidth;

function nextSlide() {
    sliderCount++;

    if (sliderCount >= sliderImages.length) {
        sliderCount = 0;
    }

    rollSlider();
}

function rollSlider() {
    sliderLine.style.transform = `translateX(${-sliderCount * sliderWidth}px)`;
}
console.log(sliderCount)
setInterval(() => {nextSlide()}, 2000);
