print('Welcome, wat is uw bestelling?')
croissantjes = int(input('Hoeveel croissantjes wil je hebben?'))
crostotaal = croissantjes * 0.39
stokbrood = int(input('hoeveel stokbrood wil je hebben?'))
stokbrodtotaal = stokbrood * 2.78
aantalkortingsbonen = int(input('Hoeveel kortingsbonnen heb je?'))
korting = int(input('Hoeveel zijn de kortingsbonnen ward?'))
kortingtotal = aantalkortingsbonen * korting / 100

totaal = stokbrodtotaal + crostotaal - kortingtotal
print({totaal},'euro')