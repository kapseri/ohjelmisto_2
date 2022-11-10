const vuosi = prompt("Anna vuosiluku")
if ((0 == vuosi % 4) && (0 != vuosi % 100) || (0 == vuosi % 400)) {
    document.querySelector('#target').innerHTML = vuosi + " is a leap year"
} else {
    document.querySelector('#target').innerHTML = vuosi + " is not a leap year"
}
