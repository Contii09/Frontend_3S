// let nome = prompt("Como voce chama?")
//
// // tres === verifica o tipo e valor
// if (nome === null) {
//     alert("Recarregue a página")
// } else {
//     let correto = confirm("Voce se chama " + nome + "?")
//
//     if (correto) {
//         alert(nome + " Bem vindo ao site de cursos")
//     } else {
//         alert("Recarregue a página")
//     }
// }

function limpaInputsLogin() {
    const inputEmail = document.getElementById('input-email')
    const inputSenha = document.getElementById('input-senha')

    inputEmail.value = ''
    inputSenha.value = ''
}

function limpaInputsCadastro() {
    const inputNome = document.getElementById('form-nome')
    const inputNascimento = document.getElementById('form-nascimento')
    const inputCpf = document.getElementById('form-cpf')
    const inputEmailL = document.getElementById('form-emaill')
    const inputSenhaa = document.getElementById('form-senhaa')
    const inputCargo = document.getElementById('form-cargo')
    const inputSalario = document.getElementById('form-salario')

    inputNome.value = ''
    inputNascimento.value = ''
    inputCpf.value = ''
    inputEmailL.value = ''
    inputSenhaa.value = ''
    inputCargo.value = ''
    inputSalario.value = ''

}


document.addEventListener("DOMContentLoaded", function () {
    const formLogin = document.getElementById('form-login')

    formLogin.addEventListener("submit", function (event) {
        // Pegar os dois inputs do formulario
        const inputEmail = document.getElementById('input-email')
        const inputSenha = document.getElementById('input-senha')

        let temErro = false

        // verificar se os inputs estao vazios
        if (inputEmail.value === '') {
            inputEmail.classList.add('is-invalid')
            temErro = true
        } else {
            inputEmail.classList.remove('is-invalid')
        }
        if (temErro) {
            // evita de enviar o form
            event.preventDefault()
            alert("Preencha todos os campos")
        }

        if (inputSenha.value === '') {
            inputSenha.classList.add('is-invalid')
            temErro = true
        } else {
            inputSenha.classList.remove('is-invalid')
        }
        if (temErro) {
            // evita de enviar o form
            event.preventDefault()
            alert("Preencha todos os campos")
        }

    })


    const formCadastro = document.getElementById('form-cadastro')

    formCadastro.addEventListener("submit", function (event) {
        // Pegar os dois inputs do formulario
        const inputNome = document.getElementById('input-nome')
        const inputNascimento = document.getElementById('input-nascimento')
        const inputCpf = document.getElementById('input-cpf')
        const inputEmailL = document.getElementById('input-emaill')
        const inputSenhaa = document.getElementById('input-senhaa')
        const inputCargo = document.getElementById('input-cargo')
        const inputSalario = document.getElementById('input-salario')

        let temErro = false

        // verificar se os inputs estao vazios
        if (inputNome.value === '') {
            inputNome.classList.add('is-invalid')
            temErro = true
        } else {
            inputNome.classList.remove('is-invalid')
        }

        if (temErro) {
            // evita de enviar o form
            event.preventDefault()
            alert("Preencha todos os campos")
        }

        // verificar se os inputs estao vazios
        if (inputNascimento.value === '') {
            inputNascimento.classList.add('is-invalid')
            temErro = true
        } else {
            inputNascimento.classList.remove('is-invalid')
        }
        if (temErro) {
            // evita de enviar o form
            event.preventDefault()
            alert("Preencha todos os campos")
        }


        // verificar se os inputs estao vazios
        if (inputCpf.value === '') {
            inputCpf.classList.add('is-invalid')
            temErro = true
        } else {
            inputCpf.classList.remove('is-invalid')
        }
        if (temErro) {
            // evita de enviar o form
            event.preventDefault()
            alert("Preencha todos os campos")
        }

        // verificar se os inputs estao vazios
        if (inputEmailL.value === '') {
            inputEmailL.classList.add('is-invalid')
            temErro = true
        } else {
            inputEmailL.classList.remove('is-invalid')
        }
        if (temErro) {
            // evita de enviar o form
            event.preventDefault()
            alert("Preencha todos os campos")
        }

        // verificar se os inputs estao vazios
        if (inputCargo.value === '') {
            inputCargo.classList.add('is-invalid')
            temErro = true
        } else {
            inputCargo.classList.remove('is-invalid')
        }
        if (temErro) {
            // evita de enviar o form
            event.preventDefault()
            alert("Preencha todos os campos")
        }

        // verificar se os inputs estao vazios
        if (inputSalario.value === '') {
            inputSalario.classList.add('is-invalid')
            temErro = true
        } else {
            inputSalario.classList.remove('is-invalid')
        }
        if (temErro) {
            // evita de enviar o form
            event.preventDefault()
            alert("Preencha todos os campos")
        }

        if (inputSenhaa.value === '') {
            inputSenhaa.classList.add('is-invalid')
            temErro = true
        } else {
            inputSenhaa.classList.remove('is-invalid')
        }
        if (temErro) {
            // evita de enviar o form
            event.preventDefault()
            alert("Preencha todos os campos")
        }


    })


})



