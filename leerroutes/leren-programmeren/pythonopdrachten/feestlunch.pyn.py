

print('Welcome, wat is uw bestelling?')
croissantjes = int(input('Hoeveel croissantjes wil je hebben?'))
croissantprijs = 39
crostotaal = croissantjes * croissantprijs
stokbrood = int(input('hoeveel stokbrood wil je hebben?'))
stokpriijs = 278
stokbrodtotaal = stokbrood * stokpriijs
aantalkortingsbonen = int(input('Hoeveel kortingsbonnen heb je?'))
korting = int(input('Hoeveel zijn de kortingsbonnen ward?'))
kortingtotal = aantalkortingsbonen * korting / 100

totaal = stokbrodtotaal + crostotaal - kortingtotal
print(f' {totaal} euro')