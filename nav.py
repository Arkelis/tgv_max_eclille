############################################################################
#  Pour l'instant, ce fichier ne contient pas de fonctions mais uniquement #
#    une suite de commandes. Il réserve manuellement en remplissant les    #
#                              formulaires.                                #
############################################################################
if __name__=="__main__":
    from splinter import Browser
    from time import sleep
    from win10toast import ToastNotifier
    import keyboard

executable_path = {'executable_path':'C:/Program Files (x86)/WebDriver/chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless = False)
## Début du script

# Aller sur le site
browser.visit("https://www.oui.sncf/")
sleep(2)
if len(browser.find_by_id("cookie-policy-close")) != 0:
    browser.find_by_id("cookie-policy-close").click()
if len(browser.find_by_id("js__ouibot-ancrage__close")) != 0:
    browser.find_by_id("js__ouibot-ancrage__close").click()

# Compléter ville d'origine
browser.find_by_id("vsb-origin-train").fill('Paris (toutes gares intramuros)')
while len(browser.find_by_text("Paris (toutes gares intramuros)")) == 0:
    sleep(0.1)
browser.find_by_text("Paris (toutes gares intramuros)").click()

# Remplissage des détails passager
browser.find_by_id("PASSENGER_1_train").click()
browser.find_by_value("YOUNG").click()
browser.find_by_id("PASSENGER_1_CARD").click()
browser.find_by_id("PASSENGER_1_CARD--option-4").click()
browser.find_by_id("PASSENGER_1_CARD-NUMBER-train").fill('300229341')
keyboard.press_and_release('tab')
keyboard.press('shift')
keyboard.write('12041997')
keyboard.release('shift')
for e in range(4): keyboard.press_and_release('left')
keyboard.write('/')
for e in range(2): keyboard.press_and_release('left')
keyboard.write('/')

# Date de départ (non fonctionnel pour l'instant)
browser.find_by_id("vsb-departure-date-train").fill('20/01/2018')

# Ville d'arrivée
browser.find_by_id('vsb-destination-train').fill('Limoges Bénédictins')
while len(browser.find_by_text("Limoges Bénédictins")) == 0:
    sleep(0.1)
browser.find_by_text("Limoges Bénédictins").click()

# Lancer la recherche
#key.tap(key.K_RETURN)
notif = ToastNotifier()
notif.show_toast("Python TGV", "Script achevé")
