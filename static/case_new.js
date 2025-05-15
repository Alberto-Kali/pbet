const slider = document.querySelector('.slider');
const sliderImages = document.querySelectorAll('.inventorys1');
const sliderLine = document.querySelector('.inventory1');
console.log(sliderImages)
let sliderCount = 0;
let sliderWidth = slider.offsetWidth;
let interval = null;

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

function openInventory() {
    const inventory = document.querySelector('.inventory');
    inventory.style.display = 'flex';
}

async function openCase(caseType) {
    try {
        const response = await fetch(`/case${caseType}open`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        if (!response.ok) {
            const errorData = await response.json();
            alert(errorData.error || 'Ошибка при открытии кейса');
            return;
        }
        const data = await response.json();
        console.log('Case opened:', data);

        // Start animation
        sliderCount = 0;
        sliderLine.style.transition = 'none';
        rollSlider();

        let maxCount = 230; // Adjust based on animation length
        interval = setInterval(() => {
            sliderCount++;
            if (sliderCount >= maxCount) {
                clearInterval(interval);
                sliderLine.style.transition = 'all 1000000s';
                openInventory();
                showPrizePopup(data.selected_item);
            }
            rollSlider();
        }, 100);

    } catch (error) {
        console.error('Error opening case:', error);
        alert('Произошла ошибка при открытии кейса');
    }
}

function showPrizePopup(item) {
    const popup = document.createElement('div');
    popup.id = 'prize-popup';
    popup.style.position = 'fixed';
    popup.style.top = '50%';
    popup.style.left = '50%';
    popup.style.transform = 'translate(-50%, -50%)';
    popup.style.backgroundColor = '#fff';
    popup.style.border = '2px solid #000';
    popup.style.padding = '20px';
    popup.style.zIndex = '1000';
    popup.style.textAlign = 'center';
    popup.innerHTML = `
        <h2>Поздравляем! Вы выиграли:</h2>
        <p>Название: ${item.name}</p>
        <p>Стоимость: ${item.cost}</p>
        <p>Редкость: ${item.rarity}</p>
        <p>Вес: ${item.weight}</p>
        <p>Цвет: <span style="color:${item.color}">${item.color}</span></p>
        <button id="close-popup-btn">Вернуться на главную</button>
    `;
    document.body.appendChild(popup);

    document.getElementById('close-popup-btn').addEventListener('click', () => {
        document.body.removeChild(popup);
        window.location.href = '/';
    });
}

// Attach event listener to open button
document.addEventListener('DOMContentLoaded', () => {
    const openBtn = document.querySelector('.butcon a.btn');
    if (openBtn) {
        openBtn.addEventListener('click', (e) => {
            e.preventDefault();
            const caseType = Number(openBtn.getAttribute('href').match(/case(\d+)/)[1]);
            openCase(caseType);
        });
    }
});
