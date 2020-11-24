""" Combinaison des trois codes présentés pour production de l'agorythme total """
# Partie 1 : Préambule
# Import 

import random
from matplotlib import pyplot as plt

# Création des objets nécéssaires aux 3 codes

class Population : # Génère une population de clients
    def __init__ (self,size) :
        self.size = int(size)
        self.orderlist = []
        self.results = {}

    def order (self,nbtour) :  # Retourne un dictionnaire référencant chaque commande par tour  
        self.nbtour = nbtour                                

        a = 1                                               
        b = 1                                               
                                                            
        while a <= self.nbtour :   
            self.orderlist.clear()
            b = 1                                           
            while b <= self.size :                          
                self.orderlist.append(random.randint(0,1))  
                b = b + 1                                   
            
            self.results[a] = repr(self.orderlist)          
            a = a + 1                                       
                                                             

class Boissons: # Genere une boisson disponible
    def __init__(self,name,price,codename):
        self.name = name
        self.price = price
        self.code_name = codename
        self.index = float()
        self.pop = 0
        self.new_order = 0
        self.new_index = float(2)
        self.choix= []

    def picpercent (self):
        self.index = (self.price / self.pop) * 10
        self.index = 10 - self.index
        self.index = round(self.index)

        compteur = 1 
        while compteur <= self.index:
            self.choix.append(self.code_name)
            compteur = compteur + 1 

    
    def refresh (self):
        self.new_index = round(self.new_index,2)
        self.price = self.price * (1 + self.new_index)
        self.price = round(self.price,2)

# Création des objets

Nzo = Population(50)

Coca = Boissons("Coca",3,1)
Water = Boissons("Water",3,2)
Beer = Boissons("Beer",3,3)

# Parametrage ExtraObjet

Water.pop = Water.price + Coca.price + Beer.price
Coca.pop = Water.pop 
Beer.pop = Water.pop 

Nb_boiss_prop = 3 

Tablebeer = []
Tablewater = []
Tablecoca = []
Tableround = []


# Programme principal
# Gen_command

Nzo.order(10)

# Gen_command avec application de la demande selon prix

compteur = 1


while compteur <= Nzo.nbtour : 
    nb_commandes = Nzo.results[compteur].count("1")
    compteur2 = 1
    commandes = []

    while compteur2 <= nb_commandes:
        Coca.picpercent()
        Water.picpercent()
        Beer.picpercent()

        Choices_left = []
        Choices_left = Coca.choix + Water.choix + Beer.choix
        final_choice = random.choice(Choices_left)
        
        commandes.append(final_choice)

        compteur2 = compteur2 + 1

    Coca.new_order = commandes.count(1)
    Beer.new_order = commandes.count(2)
    Water.new_order = commandes.count(3)

    total = Coca.new_order + Beer.new_order + Water.new_order

    moyenne_demande = 1 / Nb_boiss_prop

    Coca.new_index = (Coca.new_order / total) - moyenne_demande
    Beer.new_index = (Beer.new_order / total) - moyenne_demande
    Water.new_index = (Water.new_order / total) - moyenne_demande

    Water.refresh()
    Beer.refresh()
    Coca.refresh()

    Tablebeer.append(Beer.price)
    Tablewater.append(Water.price)
    Tablecoca.append(Coca.price)
    Tableround.append(compteur)

    compteur = compteur + 1


plt.plot(Tableround,Tablebeer, label='Beer')
plt.plot(Tableround,Tablewater,label='Water')
plt.plot(Tableround,Tablecoca, label='Coca')

plt.legend()
plt.title('Evolution of the prices of drinks overnight')
plt.ylabel('Price')
plt.xlabel('Round')

plt.show()



