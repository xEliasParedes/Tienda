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
        document.getElementById('cabecera').style.top = '-20px';
        document.getElementById('navB').style.top = '70px';
    }
    else{
        document.getElementById('cabecera').style.top = '-100px';
        document.getElementById('navB').style.top = '-100px';
    }
    ubicacionPrincipal = Desplazamiento;
}

/*--------------------------------*/
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

