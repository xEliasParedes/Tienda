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
        document.getElementById('cabecera').style.top = '0';
        document.getElementById('navB').style.top = '80px';
    }
    else{
        document.getElementById('cabecera').style.top = '-100px';
        document.getElementById('navB').style.top = '-100px';
    }
    ubicacionPrincipal = Desplazamiento;
}

