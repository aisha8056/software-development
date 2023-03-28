#Input

from tokenize import Name


name = input("Wat is uw naam?")
if name == ("Tom"):
    raise NameError ("Tom is een raree naam!")
leefttijd = int(input("Wat is uw leeftijd?"))
if leefttijd <20:
    raise NameError("Ü bent bijna bejaard")
if leefttijd <50:
    raise NameError("Awwww helaas bent je nog een baby")


diploma = input("Heb je MBO-4 Diploma gehaald?")
vrachtrijbewijs = input("Heb je vracht rijbewijs gehaald?")
geslacht = input("Bent uw een man of vrouw?")
hoed = input("Ben je in bezit van een hoge hoed?")
snor = ""
haartype = ""


if geslacht == "man":
    snor = input("Hoe breed is je snor?")
    if snor == "ja":
        snor = int(input("Hoe breed is je nor in CM?"))
elif geslacht == "vrouw":
    haartype = input("Heb je rode krullen?")
    if haartype == "ja":
        haartype = int(input("Hoe lang is uw haar?"))
length = int(input("Hoe lang ben je in CM?"))
weight = int(input("Wat is uw gewicht in KG"))
certificate = input("Heb je al certificate voor het overleven met gevaarlijk personeel?")
experience1 = int(input("Hoeveel jaar ervaring heeft uw met dieren-dressur?"))
experience2 = int(input("Hoeveel jaar ervaring heb je met jongeren kinderen?"))
expierence3 = int(input("Hoeveel jaar ervaring heb je met praktijk binnen het acrobatiek?"))

if diploma == "ja" and vrachtrijbewijs == "ja" and hoed == "ja" and (geslacht == "man" and snor > 10 or geslacht == "vrouw" and haartype >20) and length >150 and length <220 and weight >90 and weight <120 and (experience1 > 4 or experience2 > "5" or expierence3 > "3"):
    print("Uw bent aangenomen voor deze baan en je mag op gesprek komen!")
else:
    print("Helaas bent uw niet aangenomen voor deze baan. Ik wens u veel succes met uw toekomst.")



#Calculaties


#Output