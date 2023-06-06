const registro = document.getElementById('registro')
const inputs = document.querySelectorAll('#registro input')

const expresiones = {
    usuario: /^[a-zA-Z0-9\_\-]{4,16}$/,
    nombre: /^[a-zA-ZÁ-ÿ\s]{1,40}$/,
    password: /^.{4,12}$/,
    correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
    telefono: /^\d{7,14}$/

}

const validarRegistro = (e) => {
    switch (e.target.name) {
        case "usuario":
            if(expresiones.usuario.test(e.target.name)){

            } else{
                document.getElementById('grupo_usuario').classList.add('registro__grupo-incorrecto')
            }
            
        break
        case "nombre":


        break
        case "password":


        break
        case "password2":


        break
        case "correo":


        break
        case "telefono":


        break
    }

}

inputs.forEach((input) => {
    input.addEventListener('keyup', () => validarRegistro)
    input.addEventListener('blur', () => validarRegistro)
})

registro.addEventListener('submit', (e) => {
    e.preventDefault();

})