

//let weight = document.getElementById('weight')
//let height = document.getElementById('height')
//let result = document.querySelector('#result p')
//
//setInterval(() => {
//    let personWeight = Number(weight.value)
//    let personHeight = Number(height.value)
//    let imc = (personWeight / personHeight ** 2).toFixed(2)
//
//    if (imc === 'NaN' | imc === 'Infinity') {
//        result.textContent = 'Esperando preenchimento dos inputs...'
//    } else {
//        result.textContent = `Resultado do Cálculo do IMC: ${imc}`
//    }
//}, 1000)


class imcCalculator {
    constructor({weight, height, result}) {
      this.weight = weight
      this.height = height
      this.result = result
    }

    init() {
        const loop = setInterval(() => {
            const personWeight = Number(this.weight.value)
            const personHeight = Number(this.height.value)
            const imc = (personWeight / personHeight ** 2).toFixed(2)

            if (imc === 'NaN' | imc === 'Infinity') {
                this.result.textContent = 'Esperando preenchimento dos inputs...'
            } else {
                this.result.textContent = `Resultado do Cálculo do IMC: ${imc}`
            }
        }, 1000)
    }
}

const imc = new imcCalculator({
  weight: document.getElementById('weight'),
  height: document.getElementById('height'),
  result: document.querySelector('#result p')
})

imc.init()
