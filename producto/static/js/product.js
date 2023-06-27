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
        document.getElementById('img_product').style.top = '0px';

    }
    else{
        document.getElementById('cabecera').style.top = '-100px';
        document.getElementById('navL').style.top = '-100px';
        document.getElementById('navC').style.top = '-100px';
        document.getElementById('desplegable').style.width = '0px';
        document.getElementById('img_product').style.top = '520px';
   
    }
    ubicacionPrincipal = Desplazamiento;
}

/*--------------------------------*/

/*-----------------------------*/
var swiper = new Swiper(".mySwiper", {
    slidesPerView: 5,
    spaceBetween: 20,
    centeredSlides: false,
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });

