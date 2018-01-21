############################################################################
#  Pour l'instant, ce fichier ne contient pas de fonctions mais uniquement #
#    une suite de commandes. Il réserve manuellement en remplissant les    #
#                              formulaires.                                #
############################################################################
if name=="__main__":
    from splinter import Browser
    import time
    from win10toast import ToastNotifier
    import keyboard
    import ctypes
"""Ce module apporte une fonction qui redirige vers la page de réservation en
prenant en argument les villes de départ et d'arrivée, ainsi que la date de
départ.
"""

def aller_a_reservation(depart, arrivee, date, identifiant, date_naissance):
    """Fonction qui prend en argument :
        - depart (string) : la gare de départ
        - arrivee (string) : la gare d'arrivée
        - date (string) : la date de départ
    et qui ouvre chrome et envoie vers la page de réservations de billets
    automatiquement. Pour l'instant, la fonction ne choisit pas le billet exact
    mais remplit le formulaire de recherche.
    """
    notif = ToastNotifier()
    Message = ctypes.windll.user32.MessageBoxW(0, "Python va lancer Chrome pour\
 rechercher vos billets. Cette opération prendra environ 20 secondes, ne \
touchez à rien pendant jusqu'à la notification de fin.", "Python TGV", 49)
    if Message == 2:
        notif.show_toast("Python TGV", "Vous avez annulé la procédure. Python\
                          va fermer")
        exit()
    executable_path = {'executable_path':'C:/Program Files (x86)/WebDriver/chromedriver.exe'}
    #executable_path = {'executable_path':'D:/Programmes/ChromeDriver/chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless = False)
    ## Début du script
    
    # Aller sur le site
    browser.visit("https://www.oui.sncf/")
    time.sleep(5)
    if len(browser.find_by_id("cookie-policy-close")) != 0:
        browser.find_by_id("cookie-policy-close").click()
    if len(browser.find_by_id("js__ouibot-ancrage__close")) != 0:
        browser.find_by_id("js__ouibot-ancrage__close").click()
    
    # Compléter ville d'origine
    browser.find_by_id("vsb-origin-train").fill(depart)
    while len(browser.find_by_text(depart)) == 0:
        time.sleep(0.1)
    browser.find_by_text(depart).click()
    
    # Ville d'arrivée
    browser.find_by_id('vsb-destination-train').fill(arrivee)
    while len(browser.find_by_text(arrivee)) == 0:
        time.sleep(0.1)
    browser.find_by_text(arrivee).click()
    
    # Remplissage des détails passager
    browser.find_by_id("PASSENGER_1_train").click()
    browser.find_by_value("YOUNG").click()
    browser.find_by_id("PASSENGER_1_CARD").click()
    for e in range(4): keyboard.press_and_release('down')
    keyboard.press_and_release('enter')
    #browser.find_by_id("PASSENGER_1_CARD--option-4").click()
    browser.find_by_id("PASSENGER_1_CARD-NUMBER-train").fill(identifiant)
    keyboard.press_and_release('tab')
    keyboard.press('shift')
    keyboard.write(date_naissance)
    keyboard.release('shift')
    for e in range(4): keyboard.press_and_release('left')
    keyboard.write('/')
    for e in range(2): keyboard.press_and_release('left')
    keyboard.write('/')
    
    # Date de départ (non fonctionnel pour l'instant)
    browser.find_by_id("vsb-departure-date-train").fill(date)
    keyboard.press_and_release('tab')
    
    # Lancer la recherche
    # key.tap(key.K_RETURN)
    browser.click_link_by_id('vsb-booking-train-submit')
    notif.show_toast("Python TGV", "Vous allez bientôt avoir accès aux billets")
    browser.reload()
    # browser.find_by_text('TGV').first.click()    
    # time.sleep(1)
    # browser.find_by_text('Choisir ').click()
    Test = input("Appuyer sur Entrée pour terminer")
    browser.quit()

## Tests
if __name__ == '__main__':
    liste_gares = {'Paris' : 'Paris (toutes gares intramuros)', 'Limoges' :
            'Limoges Bénédictins', 'Lille' : 'Lille (toutes gares)'}
    
    identifiant = input("Entrez votre identifiant TGVmax : ")
    
    date_naissance = input("Entrez votre date de naissance au format JJMMAAAA"
                           + " sans slash ! ")
    # depart = 'Lille'
    while depart not in liste_gares:
        depart = input("Entrer la ville de départ parmi Paris, Limoges, " +
                "Lille : ")
    depart = liste_gares[depart]
    
    # arrivee = 'Paris'
    while arrivee not in liste_gares:
        arrivee = input("Entrer la ville d'arrivée parmi Paris, Limoges, " +
                "Lille : ")
    arrivee = liste_gares[arrivee]
        
    date = input("Entrer la date au format JJ/MM/AAAA : ")
    #date = '18/02/2018'
    aller_a_reservation(depart, arrivee, date, identifiant, date_naissance)
