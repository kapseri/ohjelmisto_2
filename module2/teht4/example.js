const numerot= []
let i = 1
while(i !== 0){
    i = prompt("Give a number! 0 lopettaa ohjelman")
    i = parseInt(i)
    numerot.push(i)
}
numerot.sort()
numerot.reverse()
console.log(numerot)