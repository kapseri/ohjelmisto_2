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