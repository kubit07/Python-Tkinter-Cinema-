#coding:utf-8

from tkinter import *

fenetre = Tk()
fenetre.title("Séance de Cinéma - Logiciel de gestion")
fenetre.geometry("400x300")

# fonction qui va s'activer lors du clique sur le bouton resrever
def click_btn(film_id,txt):
    print("click ok sur le film numero !",film_id)
    #choix = int(input("Inscrivez le numero du film a voir (1,2 ou 3) :"))

    print()

    print("Vos avez choisi le film : ",films[film_id-1]["titre"])

    nb_places = films[film_id-1]["places"]

# verifier si le film n'est pas complet 
    if(nb_places > 0):
        print("Achat effectué !")
        # retirer une place au nombre de palces disponibles
        films[film_id-1]["places"] -= 1
        txt.set(films[film_id-1]["places"])
        print("Le Film possède désormais :",films[film_id-1]["places"],"places")

    else:
        print("Film complet !")
        txt.set("Film Complet !")
 





# afficher un message de bienvenue 
print()
print("Bienvenue au cinema, voici les films a l'affiche:")
print()

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
    places_var = StringVar()
    places_var.set(places)


    titre_label = Label(fenetre, text=titre)
    #titre_label.pack()#va permettre de la mettre dans la fenetre tkinter
    titre_label.grid(row=numero,column=0)

    seances_label = Label(fenetre,text=seance)
    seances_label.grid(row=numero,column=1)

    places_label = Label(fenetre,textvariable=places_var)
    places_label.grid(row=numero,column=2)

    book_bouton = Button(fenetre,text="Reserver",command = lambda num = numero, txt = places_var : click_btn(num,txt))
    book_bouton.grid(row=numero,column=3)

# demande a l'utilisateur d'entrer un film a voir 
print()

fenetre.mainloop()




 

