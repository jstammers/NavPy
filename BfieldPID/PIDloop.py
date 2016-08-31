import numpy
import csv
from HardwareController import *
import time

'''
This class implements a PID loop 
'''
class PID:
    def __init__(self,P,I,D,inputChannels,outputChannels,setPoints):
        self.P = P
        self.I = I
        self.D = D
        #These can be list of values or just single entries
        self.inputChannels = inputChannels
        self.outputChannels = outputChannels
        self.setPoints = setPoints

        #Define the type of the PID
        if type(self.inputChannels) == list and type(self.outputChannels) == list:
            self.mode = "MIMO"
        elif type(self.inputChannels) == str and type(self.outputChannels) == str:
            self.mode = "SISO"
        elif type(self.inputChannels) == list and type(self.outputChannels) == str:
            self.mode = "MISO"
        elif type(self.inputChannels) == str and type(self.outputChannels) == list:
            self.mode = "SIMO"


    def run(self):
        raise NotImplementedError()

    def log(outFile, samplingRate, nSamples):
        if self.mode == "SISO":
            with open(dataPath+outFile,"wb") as csvfile:
                writer = csv.writer(dataPath+outFile,delimiter=",")
                writer.writerow(["Time","Value"])
                finished = ""
                while finished != "q":
                #This will average the data over the sampling window
                    data = hc.ReadAnalogInput(self.inputChannels,samplingRate,nSamples, true)
                    time = datetime.now().strftime("%H:%M:%S:%f")
                    writer.writerow([time,data])
                    finished = raw_input("Enter q to stop logging:")

                return "Finished logging "+ self.inputChannels + " and saved to " + outFile








     

