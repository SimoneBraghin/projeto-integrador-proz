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


//CSS da minha pag

//* pagina 5
  /* Seção sobre o café *
  .sobre-cafe {
    width: 150%;
    padding: 20px;
    background-color:#f7eee6;
  }

  .sobre-cafe img {
    width: 10%;
    margin-bottom: 10px;
  }

  /* Seção de recomendação *
  .recomendaçao{
    width: 50%;
    padding: 10px;
    background-color: #f7eee6;
  }

  .recomendaçao img {
    width: 10%;
    margin-bottom: 10px;
  }

  /* Seção de contato *
  .contato {
    width: 100%;
    padding: 12px;
    background-color: #f7eee6;
  }
  div.instagram {
  margin: 12px;
  }

  div.instagram img{
    transition: transform 0.3s ease;
    width: 50px;
    justify-content: center;
    margin: 0%;
  }
  div.instagram:hover img {
    transform: scale(1.1);
  }

    a:visited {
      color:black;
  }


  .contato img {
    width: 10%;
    margin-bottom: 10px;
  }
  /* fim pagina 5 */