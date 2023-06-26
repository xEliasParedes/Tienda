let listElements = document.querySelectorAll('.list__button--click');

listElements.forEach(listElement => {
    listElement.addEventListener('click', ()=>{
        
        listElement.classList.toggle('arrow');

        let height = 0;
        let menu = listElement.nextElementSibling;
        if(menu.clientHeight == "0"){
            height=menu.scrollHeight;
        }

        menu.style.height = `${height}px`;

    })
});

/*---------------------------------------------------------- */
let ubicacionPrincipal = window.pageYOffset;
window.onscroll = function(){
    let Desplazamiento = window.pageYOffset;
    if(ubicacionPrincipal >= Desplazamiento){
        document.getElementById('cabecera').style.top = '-22px';
        document.getElementById('navL').style.top = '70px';
        document.getElementById('navC').style.top = '70px';

    }
    else{
        document.getElementById('cabecera').style.top = '-100px';
        document.getElementById('navL').style.top = '-100px';
        document.getElementById('navC').style.top = '-100px';
        document.getElementById('desplegable').style.width = '0px';
   
    }
    ubicacionPrincipal = Desplazamiento;
}


/*---------------------------------------------------------- */

const myCarouselElement = document.querySelector('#carouselExampleCaptions2')

const carousel = new bootstrap.Carousel(myCarouselElement, {
  interval: 50000,
  touch: false
})

/*-----------------------------*/

var swiper = new Swiper("#lp1 .mySwiper", {
  slidesPerView: 5,
  spaceBetween: 20,
  centeredSlides: false,
  navigation: {
    nextEl: "#lp1 .swiper-button-next",
    prevEl: "#lp1 .swiper-button-prev",
  },
});

var swiper = new Swiper("#lp2 .mySwiper", {
  slidesPerView: 5,
  spaceBetween: 20,
  centeredSlides: false,
  navigation: {
    nextEl: "#lp2  .swiper-button-next",
    prevEl: "#lp2 .swiper-button-prev",
  },
});

var swiper = new Swiper("#lp3 .mySwiper", {
  slidesPerView: 5,
  spaceBetween: 20,
  centeredSlides: false,
  navigation: {
    nextEl: "#lp3  .swiper-button-next",
    prevEl: "#lp3 .swiper-button-prev",
  },
});


var swiper = new Swiper("#lp4 .mySwiper", {
  slidesPerView: 5,
  spaceBetween: 20,
  centeredSlides: false,
  navigation: {
    nextEl: "#lp4  .swiper-button-next",
    prevEl: "#lp4 .swiper-button-prev",
  },
});


var swiper = new Swiper("#lp5 .mySwiper", {
  slidesPerView: 5,
  spaceBetween: 20,
  centeredSlides: false,
  navigation: {
    nextEl: "#lp5  .swiper-button-next",
    prevEl: "#lp5 .swiper-button-prev",
  },
});

var swiper = new Swiper("#lp6 .mySwiper", {
  slidesPerView: 5,
  spaceBetween: 20,
  centeredSlides: false,
  navigation: {
    nextEl: "#lp6  .swiper-button-next",
    prevEl: "#lp6 .swiper-button-prev",
  },
});


  var anchoVentana = window.innerWidth

  window.onresize = function(){

    anchoVentana = window.innerWidth;
    
   
    if(anchoVentana > 1024){
      var swiper = new Swiper("#lp1 .mySwiper", {
        slidesPerView: 5,
        spaceBetween: 20,
        centeredSlides: false,
        navigation: {
          nextEl: "#lp1 .swiper-button-next",
          prevEl: "#lp1 .swiper-button-prev",
        },
      });
    
      var swiper = new Swiper("#lp2 .mySwiper", {
        slidesPerView: 5,
        spaceBetween: 20,
        centeredSlides: false,
        navigation: {
          nextEl: "#lp2  .swiper-button-next",
          prevEl: "#lp2 .swiper-button-prev",
        },
      });
    
      var swiper = new Swiper("#lp3 .mySwiper", {
        slidesPerView: 5,
        spaceBetween: 20,
        centeredSlides: false,
        navigation: {
          nextEl: "#lp3  .swiper-button-next",
          prevEl: "#lp3 .swiper-button-prev",
        },
      });
    
    
      var swiper = new Swiper("#lp4 .mySwiper", {
        slidesPerView: 5,
        spaceBetween: 20,
        centeredSlides: false,
        navigation: {
          nextEl: "#lp4  .swiper-button-next",
          prevEl: "#lp4 .swiper-button-prev",
        },
      });
    
    
      var swiper = new Swiper("#lp5 .mySwiper", {
        slidesPerView: 5,
        spaceBetween: 20,
        centeredSlides: false,
        navigation: {
          nextEl: "#lp5  .swiper-button-next",
          prevEl: "#lp5 .swiper-button-prev",
        },
      });
    
      var swiper = new Swiper("#lp6 .mySwiper", {
        slidesPerView: 5,
        spaceBetween: 20,
        centeredSlides: false,
        navigation: {
          nextEl: "#lp6  .swiper-button-next",
          prevEl: "#lp6 .swiper-button-prev",
        },
      });
    }else if(anchoVentana > 750 && anchoVentana < 1024){
      var swiper = new Swiper("#lp1 .mySwiper", {
        slidesPerView: 4,
        spaceBetween: 20,
        centeredSlides: false,
        navigation: {
          nextEl: "#lp1 .swiper-button-next",
          prevEl: "#lp1 .swiper-button-prev",
        },
      });
    
      var swiper = new Swiper("#lp2 .mySwiper", {
        slidesPerView: 4,
        spaceBetween: 20,
        centeredSlides: false,
        navigation: {
          nextEl: "#lp2  .swiper-button-next",
          prevEl: "#lp2 .swiper-button-prev",
        },
      });
    
      var swiper = new Swiper("#lp3 .mySwiper", {
        slidesPerView: 4,
        spaceBetween: 20,
        centeredSlides: false,
        navigation: {
          nextEl: "#lp3  .swiper-button-next",
          prevEl: "#lp3 .swiper-button-prev",
        },
      });
    
    
      var swiper = new Swiper("#lp4 .mySwiper", {
        slidesPerView: 4,
        spaceBetween: 20,
        centeredSlides: false,
        navigation: {
          nextEl: "#lp4  .swiper-button-next",
          prevEl: "#lp4 .swiper-button-prev",
        },
      });
    
    
      var swiper = new Swiper("#lp5 .mySwiper", {
        slidesPerView: 4,
        spaceBetween: 20,
        centeredSlides: false,
        navigation: {
          nextEl: "#lp5  .swiper-button-next",
          prevEl: "#lp5 .swiper-button-prev",
        },
      });
    
      var swiper = new Swiper("#lp6 .mySwiper", {
        slidesPerView: 4,
        spaceBetween: 20,
        centeredSlides: false,
        navigation: {
          nextEl: "#lp6  .swiper-button-next",
          prevEl: "#lp6 .swiper-button-prev",
        },
      });
    }
  };

   
