from win10toast import ToastNotifier
from splinter import Browser
from gen_url import *

config_par_defaut = ("Lille","Paris",date(2018,2,25),True)

toaster = ToastNotifier()
#toaster.show_toast("Salut",
#              "Salut Ca va mec!!",duration=10)

browser = Browser(driver_name='chrome',**{'executable_path':'C:\Program Files (x86)\WebDriver\chromedriver.exe','headless' : False})
if( bool(int(input("Modifier paramètres par défaut ? (0/1) : ")))):
    browser.visit(gen_url(*demander_args()))
else:
    browser.visit(gen_url(*config_par_defaut))

toaster.show_toast("Done!","Done!",duration=15)
browser.quit()
#toaster.on_destroy(hwnd= " HWND", msg="MSG",wparam=10,lparam=10)
