import random
import time
import sys

import colorama
#funkrioner
def attack_valet():
    val = int(input("Välj 1, 2 eller 3 för att välja ett attack: "))
    if val == 1:
        print("Du kommer att attackera med ett svärd")
    elif val == 2: 
        print("du kommer att atteckaera med ett kniv")
    elif val == 3:
        print("du kommer att atteckera med dina händer")
    else:
        print("Du måste välja 1, 2 eller 3: ")



def avsluta_spelet():
    print("Knockout! Spelet avslutas.")
    sys.exit()
#-------------------------------------------------------------------------------------------------------------------------------------
# Starta hälsopoäng
hans_hälsopoäng = 10
ditt_hälsopoäng = 10

#shop
pengar = 100

# Intro texten
print("Du är gladiatorn Livia nu ska du slåss mot gladiatorn Marcus.")
print("Ni befinner er på en romersk arena, omgivna av en entusiastisk publik.")
print("Ni har inga vapen eller rustning, utan är klädda i enkla tunikor och sandaler.")
print("ubliken som fyller läktarna ropar och skriker, deras förväntan är nästan påtaglig.")
print("Marcus står redo, hans blick är fast besluten när han tar ett steg framåt.")
print("Striden kan börja.")
print("Du har 10 coins som du kan använda när du har 4 hälso poöng kvar.")
#-------------------------------------------------------------------------------------------------------
# Spelet börjar
input("TRYCK PÅ ENTER FÖR ATT PÅBÖRJA SPELET: ")

# Stridsloopen
strid = True
while strid:
    # Din attack
    print("\nDin tur att anfalla!")
    time.sleep(1)
    attack_valet()
    dice = random.randint(1, 10)
    print("Du kastar tärningen och får:", dice)
    if dice < 4:
        print("Miss! Du missade din attack. Nu är det Marcus tur att attackera.")
    elif dice == 10:
        avsluta_spelet()
    else:
        print("Träff! Du träffade Marcus och han förlorar 2 hälsopoäng.")
        hans_hälsopoäng -= 2
        print(f"Marcus har nu {hans_hälsopoäng} hälsopoäng kvar.")
   #--------------------------------------------------------------------------------------
   
    if ditt_hälsopoäng == 4:
        svar = input("Vill du använda dina coins för att få 2 hälso poöng Y/N")
    
    if svar.upper() == "Y":
        print("du har använt upp dina coins")
        ditt_hälsopoäng += 2
    elif svar.upper() == "N":
        print("Du har valt att inte använda dina coins det är kört för dig!! ")
    else: 
        print("du måste välja Y eller N")



    # Kontrollera om Marcus har förlorat
    if hans_hälsopoäng <= 0:
        print("Du vann striden! Marcus har inga hälsopoäng kvar.")
        break

    # Marcus' attack
    input("TRYCK PÅ ENTER FÖR ATT LÅTA MARCUS ATTACKERA: ")
    print("Marcus tur att anfalla!")
    time.sleep(1)
    dice1 = random.randint(1, 10)
    print("Marcus kastar tärningen och får:", dice1)
    
    if dice1 < 4:
        print("Miss! Marcus missade sin attack.")
    elif dice1 == 10:
        print("Marcus fick Knockout! Spelet avslutas.")
        break
    else:
        print("Träff! Marcus träffade dig och du förlorar 2 hälsopoäng.")
        ditt_hälsopoäng -= 2
        print(f"Du har nu {ditt_hälsopoäng} hälsopoäng kvar.")
    
    # Kontrollera om du har förlorat
    if ditt_hälsopoäng <= 0:
        print("Marcus vann striden! Du har inga hälsopoäng kvar.")
        break

    # Statusuppdatering
    print(f"\nNuvarande hälsopoäng: Du har {ditt_hälsopoäng} och Marcus har {hans_hälsopoäng}.")

    # Ny omgång
    input("\nTRYCK PÅ ENTER FÖR ATT FORTSÄTTA TILL NÄSTA OMGÅNG: ")
    time.sleep(1)

print("\nSpelet är slut. Tack för att du spelade!")
