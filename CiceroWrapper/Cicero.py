'''
A wrapper class for Cicero Word Generator
'''
from settings import *
import WordGenerator as netCicero
class Cicero:
    def __init__(self):
        '''
        Initialises an instance of Cicero
        '''
        self.sequence = None
        self.server = None
        self.cicero = netCicero
        self.cicero.MainClientForm()
        self.load_settings()

    def load_settings(self):
        self.settings = self.cicero.Storage.SaveAndLoad.LoadSettingsData(ciceroSettings + "SettingsData.json")

    def load_sequence(self,filename):
        if os.path.exists(ciceroSettings+filename):
            self.sequence = self.cicero.Storage.SaveAndLoad.LoadSequenceToStorage(ciceroSettings+filename)
        else:
            return "Sequence File Not Found"


