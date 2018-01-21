if __name__ == "__main__":
    from splinter import Browser



class Trajet:
    
    def __init__(self, id_sncf=None, id_bdd=None, gdep=None,
                 garr=None, hdep=None, date=None,
                 dur=None, option=None, nb=None):
        self.id_train_sncf = id_sncf
        self.id_tj_bdd = id_bdd
        self.g_dep = gdep
        self.g_arr = garr
        self.d_dep = d
        self.h_dep = hdep
        self.duree = dur
        self.option_trajet = option
        self.nb_places = nb
    
    @staticmethod
    def lire_page(browser):
        liste_traj = []    
        traj_lu = Trajet()

    def __str__(self):
        print("Gare de départ : " + self._dep)
        print("Gare d'arrivée : " + self.g_arr)
        print("Heure de départ : " + self.h_dep)
        print("Durée de trajet : " + self.duree)
        print("Option de trajets : " + self.option_trajet)
        print("Nb de places dispo : " + self.nb_places)

   
