if name == "__main__":
    from splinter import Browser



class Trajet():
    

    def __init__(self,id_sncf=None ,id_bdd=None,gdep=None,garr=None,hdep=None,date=None,dur = None,option=None,nb=None):
        
        id_train_sncf = id_sncf
        id_tj_bdd; = id_bdd
        g_dep= gdep
        g_arr = garr
        d_dep = d
        h_dep = hdep
        duree = dur
        option_trajet= option
        nb_places =nb
    
    @staticmethod
    def lire_page(browser):
        liste_traj = []    
        traj_lu = Trajet()

    def __str__(self):
        print("Gare de départ : " + g_dep)
        print("Gare d'arrivée : " + g_arr)
        print("Heure de départ :" + h_dep)
        print("Durée de trajet :" + duree)
        print("Option de trajets :" + option_trajet)
        print("Nb de places dispo :" +nb_places)
    


   
