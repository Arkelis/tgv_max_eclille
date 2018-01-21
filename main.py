from win10toast import ToastNotifier #A installer (pip)
from splinter import Browser         #A installer (pip)
from time import sleep
from datetime import timedelta
import keyboard
from gen_url import *
#from nav import *
from trajet import *
from bdd import *


recherche_par_defaut = ("Lille","Paris",date.today()+timedelta(15),True)
recherche= recherche_par_defaut


toaster = ToastNotifier()

browser = Browser(driver_name='chrome',**{'executable_path':'C:\Program Files (x86)\WebDriver\chromedriver.exe','headless' : True})


if( bool(int(input("Modifier recherche par défaut ? (0/1) : ")))):
    recherche = demander_args()

#Tant qu'on n'a pas obtenu une date où des TGV MAX ont été publiés
#On redemande un nouveau trajet
while(recherche[rech['JDEP']] > date.today()+timedelta(30)):
    print("\nERREUR : les TGV Max sont publiés seulement 30 jours à l'avance !")
    print("Essayez une autre recherche !\n")
    if( bool(int(input("Modifier recherche par défaut ? (0/1) : ")))):
        recherche = demander_args()


browser.visit(gen_url(*recherche))
    
while(len(browser.find_by_id(get_IdDuJour(recherche[rech['JDEP']])))==0):
    sleep(1)

browser.find_by_id(get_IdDuJour(recherche[rech['JDEP']])).click()

toaster.show_toast("Done!","Done!",duration=15)

#toaster.on_destroy(hwnd= " HWND", msg="MSG",wparam=10,lparam=10)
