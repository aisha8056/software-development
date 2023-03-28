#input

afmeting = input('Kies de grootte: small, medium, large ')  
try:
    aantal = int(input("Hoeveel pizza's wilt u hebben? ")) 
except:
    print("Sorry Hij werkt niet")

#calculaties


afmeting in("s","small","Small","S"):
    prijs = 5.99
afmeting in("m","medium","Medium","M"):
    prijs = 7.99
afmeting in("l","large","Large","L"):
    prijs = 12.99

totaalprijs = aantal * prijs

print(f"""
    BON
    -------------------------------------
    {aantal} {afmeting} pizza's       {aantal}x {prijs},- €
    
    -------------------------------------
    Totaal prijs:           {totaalprijs},- €
    """) # Hier krijgt de persoon die heeft de pizza's besteld.