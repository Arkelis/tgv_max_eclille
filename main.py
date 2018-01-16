from win10toast import ToastNotifier
from splinter import Browser


toaster = ToastNotifier()
#toaster.show_toast("Salut",
#              "Salut Ca va mec!!",duration=10)

browser = Browser(driver_name='chrome',headless = True,**{'executable_path':'C:\Program Files (x86)\WebDriver\chromedriver.exe'})

browser.visit("https://www.oui.sncf/bons-plans/tgvmax#!/FRLIL/FRPAR/20180127/ONE_WAY/2/12-HAPPY_CARD?onlyDirectTrains=true&lang=fr*")

toaster.show_toast("Done!","Done!",duration=15)
browser.quit()
toaster.on_destroy(hwnd= " HWND", msg="MSG",wparam=10,lparam=10)
