import pandas as pd

class DataCloner:

    def cloneCsvData(self):
        self.dataConfirmed = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv', error_bad_lines=False)
        self.dataDeaths = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv', error_bad_lines=False)
        self.dataRecovered = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv', error_bad_lines=False)

    def testPrint(self):
        print (self.dataConfirmed)
        print (self.dataDeaths)
        print (self.dataRecovered)
