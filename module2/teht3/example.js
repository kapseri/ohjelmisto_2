const koirat = []
let i = 0
while(i < 6){
    koirat[i] = prompt("Anna koiran nimi");
    i +=1
}

i = 0
koirat.sort();
koirat.reverse();
while(i < 6){
var node = document.createElement('li');
node.appendChild(document.createTextNode(koirat[i]));
 
document.querySelector('ul').appendChild(node);
i+=1
}