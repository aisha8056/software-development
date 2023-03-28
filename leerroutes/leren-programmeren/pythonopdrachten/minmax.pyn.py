#Input


A = input ("Vul een getal in!")
B = input ("Vul nogmaals een getal in!")


#Calculaties 

if A > B:
    max = A
    min = B
    print (f"A is natuurlijk het grootste getal: {max}")
elif B > A:
    max = B
    min = A
    print(f"A is natuurlijk het klienste getal: {min}")
else:print("A en B zijn het zelfde")
print(f"Het maximun is {max}")
print(f"Het minimum is {min}")

#Output

#Hier kan je zien het max and min progamma!