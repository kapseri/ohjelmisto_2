const luku1 = prompt("luku1");
const luku2 = prompt("luku2");
const luku3 = prompt("luku3");
let sum = parseInt(luku1) + parseInt(luku2) + parseInt(luku3);
let average = sum / 3;
document.querySelector('#target').innerHTML = 'Sum is ' + sum + ' Average is '+ average;