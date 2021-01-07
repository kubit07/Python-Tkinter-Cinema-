#coding:utf-8
# afficher un message de bienvenue 
print()
print("Bienvenue au cinema, voici les films a l'affiche:")
print()
  
# liste de films
#films = ["Voyage au centre du HTML","Les 9 jsons cachés","Algobox - le film"]

# Version avec le dictionnaire 
films =  [
    { # film 1
        "titre" : "Voyage au centre du HTML",
        "seance" : "18h:05",
        "places" : 200   
    },
    { # film 2
        "titre" : "Les 9 jsons cachés",
        "seance" : "10h:10",
        "places"  : 80 
    },
    { # film 3
        "titre" : "Algobox - le film",
        "seance" : "22h:15",
        "places" :  1 
    }
]

# afficher chaque film
for numero,film in enumerate(films,start=1):
    #print("Film numéro ",numero," nom : ",film["titre"]," seance : ",film["seance"],"(",film["places"],"places dipo )")
    titre = film["titre"]
    seance = film["seance"]
    places = film["places"]

    print(f"Film numero {numero} : {titre} : seance : {seance} ({places} places dispo)")

#boucle 
while True:

        # demande a l'utilisateur d'entrer un film a voir 
    print()
    choix = int(input("Inscrivez le numero du film a voir (1,2 ou 3) :"))

    # controle sur le choix du film a voir
    while(choix<1 or choix>3):
        choix = int(input("Inscrivez le numero du film a voir (1,2 ou 3) :"))

    print()

    print("Vos avez choisi le film : ",films[choix-1]["titre"])

    nb_places = films[choix-1]["places"]

    # verifier si le film n'est pas complet 
    if(nb_places > 0):
        print("Achat effectué !")
        # retirer une place au nombre de palces disponibles
        films[choix-1]["places"] -= 1
        print("Le Film possède désormais :",films[choix-1]["places"],"places")
    else:
        print("Film complet !")




 

