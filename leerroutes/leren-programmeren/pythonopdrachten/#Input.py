#Input

pizzasizesmall = "Small Pizza"
prijssmallpizza = 5
pizzamedium = "Medium Pizza"
prijsmediumpizza = 8
pizzasizebig = "Big Pizza"
prijsbigpizza = 12

#Calculaties 

print(pizzasizesmall)
aantal_pizzasmall = int(input("Hoeveel:"))
print(prijssmallpizza)
prijssmalltotaal = prijssmallpizza * aantal_pizzasmall
print(type(prijssmalltotaal))


print(pizzamedium)
hoeveelpizzamedium = int(input("Hoeveel"))
print(prijsmediumpizza)
prijsmediumtotaal = prijsmediumpizza * hoeveelpizzamedium
print(type(prijsmediumtotaal))

print(pizzasizebig)
hoeveelbigpizza = int(input("Hoeveel"))
print (pizzasizebig)
pizzabigtotaal = prijsbigpizza * hoeveelbigpizza
print(type(pizzabigtotaal))
totaleprijs =  pizzabigtotaal + prijsmediumtotaal + prijssmalltotaal


print('--------------------------------------------------------------')
print(f'| U heeft {aantal_pizzasmall} small pizza besteld:  {prijssmalltotaal} ')
print(f'| U heeft {hoeveelpizzamedium} small pizza besteld:  {prijsmediumtotaal} ')
print(f'| U heeft {hoeveelbigpizza} small pizza besteld:  {pizzabigtotaal} ')
print(f' Uw totaal prijs is {totaleprijs} euro')

print('--------------------------------------------------------------')



#Output





