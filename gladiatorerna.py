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
msvcrt.getch()
strid = 1
while strid:
    
    dice = random.randint(1,10)

    if dice <= 3:
     resultat = "miss"
    elif dice > 3:
     resultat = "träff"

# Gör att motståanden kan anfalla

# presentera vem som vann