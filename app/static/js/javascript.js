var input = document.querySelector('#id_cpf')
var input2 = document.querySelector('#id_cep')
var input3 = document.querySelector('#id_pis')

input.addEventListener('keypress', () => {
    let inputLength = input.value.length
    if (inputLength == 3 || inputLength == 7) {
        input.value += '.'
    }else if (inputLength == 11) {
        input.value += '-'
    }
})

input2.addEventListener('keypress', () => {
    let input2Length = input2.value.length
    if (input2Length == 5) {
        input2.value += '-'
    }})

input3.addEventListener('keypress', () => {
    let input3Length = input3.value.length
    if (input3Length == 3 || input3Length == 9) {
        input3.value += '.'
    }else if (input3Length == 12) {
        input3.value += '-'
    }
})