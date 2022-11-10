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
