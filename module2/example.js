let nopat = prompt("number of dice")
nopat = parseInt(nopat)
let luku = prompt("sum of the eye numbers")
luku = parseInt(luku)
let prosentti = 0
let noppa = 0
let summa = 0
let x = 1
let n = 0
while(x <= 100000){
    while(n < nopat){
        noppa = Math.floor(Math.random()*6+1)
        summa += noppa
        n += 1
    }
    if (summa == luku)
        prosentti += 1
        summa = 0
    summa = 0
    x += 1
    n = 0
}
prosentti = prosentti / 1000
prosentti = parseFloat(prosentti).toFixed(2);
document.querySelector('#target').innerHTML ="Probability to get sum " +luku+" with "+nopat+" dice is "+prosentti+"%";