const heitot = []
function diceRoll(){
 return Math.floor(Math.random()*6+1)
}

let noppa = 0
while (noppa != 6){
    noppa = diceRoll()
    heitot.push(noppa)
}
i = 0
while(i < heitot.length){
    var node = document.createElement('li');
    node.appendChild(document.createTextNode("Heitto" + (i+1) + ": " + heitot[i]));
     
    document.querySelector('#target').appendChild(node);
    i+=1
    }