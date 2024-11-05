import random
import time
import sys

def avsluta_spelet():
    print("Du fick Knockout avsluta spelet")
    sys.exit()

# Starta hälsopoäng
hans_hälsopoäng = 10
ditt_hälsopoäng = 10

# Intro texten
print("Du är gladiatorn Livia, nu ska du slåss mot gladiatorn Marcus.")
print("Ni befinner er på en romersk arena, omgivna av en entusiastisk publik.")
print("Ni har inga vapen eller rustning, utan är klädda i enkla tunikor och sandaler.")
print("Publiken som fyller läktarna ropar och skriker, deras förväntan är nästan påtaglig.")
print("Marcus står redo, hans blick är fast besluten när han tar ett steg framåt.")
print("Striden kan börja.")

# Spelet börjar
input("TRYCK PÅ ENTER FÖR ATT PÅBÖRJA SPELET: ") 

strid = True
while strid:
    # Din attack
    print("\nDin tur att anfalla!")
    time.sleep(1)
    dice = random.randint(1, 10)
    print("Du kastar tärningen och får:", dice)
    
    if (dice < 4 and dice < 10 ):
        print("Miss! Du missade din attack. Nu är det Marcus tur att attackera.")
    if dice == 10:
        avsluta_spelet()
 
    else:
        print("Träff! Du träffade Marcus och han förlorar 2 hälsopoäng.")
        hans_hälsopoäng -= 2
        print(f"Marcus har nu {hans_hälsopoäng} hälsopoäng kvar.")
    
    # Kontrollera om Marcus har förlorat
    if hans_hälsopoäng <= 0:
        print("Du vann striden! Marcus har ing(a hälsopoäng kvar.")
        break
 
    # Marcus' attack
    input("TRYCK PÅ ENTER FÖR ATT LÅTA MARCUS ATTACKERA: ") 
    print("Marcus tur att anfalla!")
    time.sleep(1)
    dice1 = random.randint(1, 10)
    print("Marcus kastar tärningen och får:", dice1)
    
    if (dice1 < 4 and dice1 < 10):
        print("Miss Marcus missade sin attack.")
    if dice == 10:
         avsluta_spelet()
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
