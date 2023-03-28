#Input

#In deze progamma zou je kaas kunnen bestellen en wij gaat kijken welte kaas je wilt!


#Calculaties

geel = input("Is de kaas geel? (ja/nee)")
if geel == "ja":
    gaten = input("Zitten er gatten in? (ja/nee)")
    if gaten == "ja":
        duur = input("Is de kaas belachelijk duur?")
        if duur == "ja":
             print("Emmenthaler")
        elif duur == "nee":
            print("Leerdammer")
    elif gaten == "nee":
            steenkaas = input("Is de kaas hard als steen? ja/nee")
            if steenkaas == "ja":
                print("Parmigiano Reggiano")
            elif steenkaas == "nee":
                print("Goudse Kaas")
elif geel == "nee":
    blauwekaas = input("Heeft de kaas blauwe schimmel? ja/nee")
    if blauwekaas == "ja":
        korstkaas = input("Heeft de kaas een korst? ja/nee")
        if korstkaas == "ja":
             print("Blue de Rochbaron")
        elif korstkaas == "nee":
                print("Foume d'Ambert")
    elif blauwekaas == "nee":
            kaaskorst2 = input("Heeft de kaas een korst? ja/nee")
            if kaaskorst2 == "ja":
                print("Camembert")
            elif kaaskorst2 == "nee":
                print("Mozzarella")
 





# if schimmel == "ja":
#     korst = input("Heeft de kaas korst? (ja/nee)")

# if korst == "ja":
#     print("Blue de Rochbaron")

# else:
#     print ("Foume d'Ambert")

# else: 
# korst = input("Heeft de kaas korst? (ja/nee)")

# if korst == "ja":
#     kaasstinkt =input("Hoe ruikt de kaas? Stinkt de kaas? (ja/nee)")

# if kaasstinkt =="ja": 

# print("Camembert")

# else:
# print ("Mozzarella")


# #Output

# #Nu ben je aan het eind van deze programma!