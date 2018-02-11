import pandas as pd
import requests as rq
import io
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from functools import partial
from Tools import time_difference


class DataProcessing():

    def __init__(self):
        """
        Quelques trucs a décommenter pour la version finale (version dev plus rapide en chargeant le fichier deja traite directement)
        """
        #file_downloaded = rq.get("https://ressources.data.sncf.com/explore/dataset/tgvmax/download/?format=csv&timezone=Europe/Berlin&use_labels_for_header=true")
        #self.data = pd.read_csv(io.StringIO(file_downloaded.text),sep=";")
        #self.data.to_csv("data.csv",index=False)
        self.data=pd.read_csv("data.csv",sep=",")
        #self.data=self.add_column("Durée",self.data)
        #self.data.to_csv("data.csv", index=False)

    def add_column(self, column, doc):
        if column == "Durée":
            duree = []
            FMT = '%H:%M'
            for i in range(len(doc["DATE"])):
                dep = doc["Heure_depart"].iloc[i]
                arr = doc["Heure_arrivee"].iloc[i]
                duree.append(time_difference(dep, arr, "h%m"))
            doc["Durée du trajet"] = pd.Series(duree)
            return doc


    def availability_on_travel(self, criteria):
        """
        Determine the dataframe asociated with the date,origin and destination given. It can determine an empty dataframe.
        :param date: string
        :param origin: string
        :param destination: string
        :return: pandas.dataframe
        """
        result=self.data[(self.data["DATE"]==criteria["DATE"])&(self.data["Origine"]==criteria["Origine"])&(self.data["Destination"]==criteria["Destination"])]
        return result.drop(["ENTITY","Axe","Origine IATA","Destination IATA","CODE_EQUIP"],axis=1)

class CitySelector(Popup):

    def __init__(self, **kwargs):
        super(CitySelector, self).__init__(**kwargs)

    def select_city(self,city):
        self.City = city
        self.dismiss()

class DaySelector(Popup):

    def __init__(self, **kwargs):
        super(DaySelector, self).__init__(**kwargs)

    def select_day(self,day):
        self.Day = day
        self.dismiss()

class MonthSelector(Popup):

    def __init__(self, **kwargs):
        super(MonthSelector, self).__init__(**kwargs)

    def select_month(self,month):
        self.Month = month
        self.dismiss()

class YearSelector(Popup):

    def __init__(self, **kwargs):
        super(YearSelector, self).__init__(**kwargs)

    def select_year(self,year):
        self.Year = year
        self.dismiss()

class MainMenu(FloatLayout):

    def __init__(self, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        self.doc = DataProcessing()
        self.criteria = {}

    def load_CitySelector(self, mode):
        self.CityPopup = CitySelector(title='Choose the departure city', size_hint=(0.9, 0.9))
        self.CityPopup.open()
        self.CityPopup.bind(on_dismiss=partial(self.get_city,mode))

    def get_city(self,mode,*args):
        if mode == "departure":
            self.criteria["Origine"] = self.CityPopup.City
        else:
            self.criteria["Destination"] = self.CityPopup.City

    def load_DaySelector(self):
        self.DayPopup = DaySelector(title='Choose the day date', size_hint=(0.9, 0.9))
        self.DayPopup.open()
        self.DayPopup.bind(on_dismiss=partial(self.get_day))

    def get_day(self,*args):
        self.day = self.DayPopup.Day

    def load_MonthSelector(self):
        self.MonthPopup = MonthSelector(title='Choose the day date', size_hint=(0.9, 0.9))
        self.MonthPopup.open()
        self.MonthPopup.bind(on_dismiss=partial(self.get_month))

    def get_month(self,*args):
        self.month = self.MonthPopup.Month

    def load_YearSelector(self):
        self.YearPopup = YearSelector(title='Choose the day date', size_hint=(0.9, 0.9))
        self.YearPopup.open()
        self.YearPopup.bind(on_dismiss=partial(self.get_year))

    def get_year(self,*args):
        self.year = self.YearPopup.Year

    def show_result(self):
        self.criteria["DATE"] = self.year+" - "+self.month+" - "+self.day
        print(self.criteria)
        txt=self.doc.availability_on_travel(self.criteria).to_csv(index=False)
        self.ids["txt_inpt"].text = txt.replace(",","  ")

class ReservationTGVmax(App):
    def build(self):
        return MainMenu()


if __name__ == '__main__':
    ReservationTGVmax().run()
