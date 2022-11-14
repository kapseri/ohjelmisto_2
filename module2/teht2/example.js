const porukka = []
const lukum = prompt('Number of people');
let i = 0
while(i < parseInt(lukum)){
    porukka[i] = prompt("Anna nimi");
    i +=1
}

i = 0
while(i < parseInt(lukum)){
var node = document.createElement('li');
node.appendChild(document.createTextNode(porukka[i]));
 
document.querySelector('ol').appendChild(node);
i+=1
}