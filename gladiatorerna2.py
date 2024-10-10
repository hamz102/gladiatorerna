import random
import msvcrt
# Intro texten 


print("Du är gladiatorn Livia, nu ska du slåss mot gladiatorn Marcus.")
print("Ni befinner er på en romersk arena, omgivna av en entusiastisk publik.")
print("Ni har inga vapen eller rustning, utan är klädda i enkla tunikor och sandaler. Ditt svarta hår fladdrar i vinden, och en halskedja av järn glimmar runt din hals.")
print("Din muskulösa kropp glänser i svetten under den varma solen.")
print("Publiken som fyller läktarna ropar och skriker, deras förväntan är nästan påtaglig.")
print("Marcus står redo, hans blick är fast besluten när han tar ett steg framåt.")
print("Striden kan börja.")

# Spelearen kan anfalla
input("TRYCK PÅ ENTER")             # Väntar på att spelaren trycker på enter. Ingen koppling med while

strid = True
while strid == True:
    dice = random.randint(1,10)
    print (dice)
    
    if (dice <= 5):
        resultat = "Miss"
        print (resultat, "du har missat det är hans attack nu")
    elif dice > 5:
        resultat = "Träff"
        print (resultat, "bra du har minskat två av hans hälsopoöng det är hans attack nu ")
    
    strid  = False
if not strid == False:
    print("Nu är hans tur nu att attackera 😥 ")
if dice <= 5:
    print("han har 8 hälsopoöng och han kommer att attackera dig nu")
    elese:
        print("han har 10 hälsopoöng och kommer att attackera dig nu")


verktyg1 = input("välj ett siffra 1, 2, 3: ")
if verktyg1 == 1:
     print("han kommer att attackera dig med ett pistol")
elif verktyg1 == 2:
    print("han kommer att attackera dig med svärd")
elif verktyg1 == 3:
    print("Du har bra tur han kommer att attackera dig med sina händer")
    else:
    print("Ogiltigt val, försök igen.")
# Gör att motståanden kan anfalla



# presentera vem som vann