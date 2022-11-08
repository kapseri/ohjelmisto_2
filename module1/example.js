/*
Tehtävä 1:
console.log("I'm printing to console!");

Tehtävä 2:
const name = prompt('Type your name.');
document.querySelector('#target').innerHTML = 'Hello, ' + name + '!';

Tehtävä 3:
const luku1 = prompt("luku1");
const luku2 = prompt("luku2");
const luku3 = prompt("luku3");
let sum = parseInt(luku1) + parseInt(luku2) + parseInt(luku3);
let average = sum / 3;
document.querySelector('#target').innerHTML = 'Sum is ' + sum + ' Average is '+ average;

Tehtävä 4:
const name = prompt('Type your name.');
let num = Math.floor(Math.random()*4)+1;
if (num == 1){
    document.querySelector('#target').innerHTML = name + ", you are Daredevil!";
}
else if(num == 2){
    document.querySelector('#target').innerHTML = name + ", you are Slytherin!";
}
else if(num == 3){
    document.querySelector('#target').innerHTML = name + ", you are Hufflepuff!";
}
else if(num == 4){
    document.querySelector('#target').innerHTML = name + ", you are Ravenclaw!";
}
else{
    document.querySelector('#target').innerHTML ="Nyt meni jotain pahasti pieleen..";
}

Tehtävä 5:

const vuosi = prompt("Anna vuosiluku")
if ((0 == vuosi % 4) && (0 != vuosi % 100) || (0 == vuosi % 400)) {
    document.querySelector('#target').innerHTML = vuosi + " is a leap year"
} else {
    document.querySelector('#target').innerHTML = vuosi + " is not a leap year"
}

Tehtävä 6:

let luku = 0;
const answer = confirm("Should I calculate the square root?");
if (answer == true){
    luku = prompt("Insert number")
    if (luku >= 0){
        nel = Math.sqrt(luku)
        document.querySelector('#target').innerHTML ="The Square root of "+luku+" is "+nel;
    }
    else{
        document.querySelector('#target').innerHTML ="The square root of a negative number is not defined";
    }
}
else{
    document.querySelector('#target').innerHTML ="The square root is not calculated.";
}

Tehtävä 10:

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
*/