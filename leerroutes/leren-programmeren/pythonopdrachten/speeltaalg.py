#input

ticketprijs = 7.45
aantalpersonen = 4
aantalminuten = 45
totaalticketprijs = 7.45 * aantalpersonen

#calculaties

vr = ((aantalminuten/5) * 0.37) * aantalpersonen
totaalbedrag = totaalticketprijs + vr

totaalbedrag = round(totaalticketprijs + vr, 2)
#output
print (f"Dagje uit met {aantalpersonen} personen in de speelhal duurt {aantalminuten} minuten. En dat kost {totaalbedrag} euro")
