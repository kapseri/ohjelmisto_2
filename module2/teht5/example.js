const numerot= []
let i = 0
while (true){
    i = prompt("Give a number! pt2")
    i = parseInt(i)
    if (numerot.includes(i) == true)
     break
    if (numerot.includes(i) == false)
        numerot.push(i)
}
alert("The number has already been given")
numerot.sort(function (a, b) {  return a - b;  });
console.log(numerot)