#input

ticketprijs = 745
aantalpersonen = 4
aantalminuten = 45
vrprijs = 37
totaalticketprijs = ticketprijs * aantalpersonen

#calculaties

vr = ((aantalminuten/5) * vrprijs) * aantalpersonen
totaalbedrag = totaalticketprijs + vr

totaalbedrag = round(totaalticketprijs + vr, 2)
#output
print (f"Dagje uit met {aantalpersonen} personen in de speelhal duurt {aantalminuten} minuten. En dat kost {totaalbedrag} euro")
