from win10toast import ToastNotifier
from splinter import Browser
from gen_url import *
from time import sleep


recherche_par_defaut = ("Lille","Paris",date.today(),True)
recherche= recherche_par_defaut

toaster = ToastNotifier()
#toaster.show_toast("Salut",
#              "Salut Ca va mec!!",duration=10)

browser = Browser(driver_name='chrome',**{'executable_path':'C:\Program Files (x86)\WebDriver\chromedriver.exe','headless' : False})
if( bool(int(input("Modifier recherche par défaut ? (0/1) : ")))):
    config = demander_args()

browser.visit(gen_url(*recherche))
    
while(len(browser.find_by_id(get_IdDuJour(recherche[rech['JDEP']])))==0):
    sleep(1)

browser.find_by_id(get_IdDuJour(recherche[rech['JDEP']])).click()

toaster.show_toast("Done!","Done!",duration=15)

#toaster.on_destroy(hwnd= " HWND", msg="MSG",wparam=10,lparam=10)
