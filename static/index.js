// Инициализация всплывающих подсказок Bootstrap
document.addEventListener('DOMContentLoaded', function() {
  // Включение всех всплывающих подсказок
  const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
  tooltipTriggerList.map(function (tooltipTriggerEl) {
      return new bootstrap.Tooltip(tooltipTriggerEl);
  });
  
  // Параллакс эффект для герой-секции
  const heroSection = document.querySelector('.hero-section');
  if (heroSection) {
      window.addEventListener('scroll', function() {
          const scrollPosition = window.pageYOffset;
          heroSection.style.backgroundPositionY = scrollPosition * 0.5 + 'px';
      });
  }
  
  // Анимация при загрузке кейсов
  const caseCards = document.querySelectorAll('.case-card');
  caseCards.forEach((card, index) => {
      card.style.opacity = '0';
      card.style.transform = 'translateY(20px)';
      card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
      
      setTimeout(() => {
          card.style.opacity = '1';
          card.style.transform = 'translateY(0)';
      }, 100 + (index * 100));
  });
});

// Показ уведомления при добавлении в корзину (пример)
function showCaseNotification(caseNumber) {
  const notification = document.createElement('div');
  notification.className = 'position-fixed bottom-0 end-0 p-3';
  notification.style.zIndex = '9999';
  
  const toast = document.createElement('div');
  toast.className = 'toast show';
  toast.role = 'alert';
  toast.setAttribute('aria-live', 'assertive');
  toast.setAttribute('aria-atomic', 'true');
  
  toast.innerHTML = `
      <div class="toast-header bg-primary text-white">
          <strong class="me-auto">ИхтиоБет</strong>
          <button type="button" class="btn-close btn-close-white" data-bs-dismiss="toast" aria-label="Close"></button>
      </div>
      <div class="toast-body bg-dark">
          Кейс ${caseNumber} добавлен в корзину!
      </div>
  `;
  
  notification.appendChild(toast);
  document.body.appendChild(notification);
  
  // Автоматическое скрытие через 3 секунды
  setTimeout(() => {
      toast.classList.remove('show');
      setTimeout(() => {
          notification.remove();
      }, 300);
  }, 3000);
}