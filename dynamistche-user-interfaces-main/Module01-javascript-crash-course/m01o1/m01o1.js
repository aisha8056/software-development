let uitleg = "In een parkeergarage passen 80 auto's op de begane grond en 120 op een verdieping.\n" +
    "Vraag het gewenste aantal auto's in de garage en bereken het aantal verdiepingen wat je nodig hebt.";

alert(uitleg);

let gewenste_aantal_autos = prompt("Hoeveel autos wilt u kwijt in de parkeergarage?");

let aantal_verdiepingen = Math.ceil((gewenste_aantal_autos - 80) / 120);
// Berekenen hier het aantal verdiepingen

if (aantal_verdiepingen < 0) {
    aantal_verdiepingen = 0;
}

let antwoord = "Om het gewenste aantal auto's kwijt te kunnen, heb je " + aantal_verdiepingen + " verdieping(en) nodig.";
document.getElementById("antwoord").innerText = antwoord;

console.log("Om het gewenste aantal auto's kwijt te kunnen heb ik " + aantal_verdiepingen + " verdiepingen nodig.");

document.write("<p>" + antwoord + "</p>");

window.alert(antwoord);
