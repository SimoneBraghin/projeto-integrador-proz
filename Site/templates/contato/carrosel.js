  let index = 0;
  let carrosselInterval; 

  function nextSlide() {
      const carousel = document.getElementById('carousel');
      index = (index + 1) % totalSlides;
      carousel.style.transform = `translateX(-${index * 50}%)`;
  }

  function prevSlide() {
      const carousel = document.getElementById('carousel');
      index = (index - 1 + totalSlides) % totalSlides;
      carousel.style.transform = `translateX(-${index * 50}%)`;
  }

  function startAutoCarousel() {
    carrosselInterval = setInterval(nextSlide, 3000); 
  }

  function stopAutoCarousel() {
    clearInterval(carrosselInterval); 
  }

  document.getElementById('nextButton').addEventListener('click', nextSlide);
  document.getElementById('prevButton').addEventListener('click', prevSlide);

  const carousel = document.getElementById('carousel');
  carousel.addEventListener('mouseenter', stopAutoCarousel);
  carousel.addEventListener('mouseleave', startAutoCarousel);

  window.onload = startAutoCarousel;

  const totalSlides = document.querySelectorAll('.carousel-slide').length;
