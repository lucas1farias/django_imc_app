

let inks = ['black', '#222', '#444']
let angles = ['45deg', '-45deg', '90deg', '-90deg', '120deg', '-120deg', '180deg', '-180deg']

const loop = setInterval(() => {
    inks.sort(function() {return Math.random() - 0.5})
    let angle = Math.floor(Math.random() * angles.length)
    document.body.style.backgroundImage = `linear-gradient(${angles[angle]}, ${inks[0]}, ${inks[1]}, ${inks[2]})`
}, 1000)
