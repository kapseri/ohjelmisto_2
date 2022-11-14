const porukka = []
const lukum = prompt('Number of candidates');

for(i = 1; i <= lukum; ++i) {
    nimi = prompt("Name of candidate " + i)
    porukka[i]
            = { 
                name: nimi, 
                votes: 0
              }; 
   }

const voters = prompt('Number of voters');
for(i = 0; i < voters; ++i) {
    nimi = prompt("Name of a candidate")
    let x = 1
    while(x <= lukum){
        if (nimi == porukka[x].name){
            porukka[x].votes += 1
        }
        x +=1
    }
}

porukka.sort(({votes:a}, {votes:b}) => b-a);

console.log("The winner is " + porukka[0].name + " with " + porukka[0].votes + " votes.")

console.log("results:")
for(i = 0; i < lukum; ++i) {
    console.log(porukka[i].name+": "+porukka[i].votes+" votes")
}