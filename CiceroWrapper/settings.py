'''
A settings file containing default paths
'''
import clr
clr.AddReference("System.Collections")
from System import String
from System.Collections import *
import sys
ciceroSettings = "C:\\Users\\Navigator\\Settings\\Cicero\\"
sys.path.append("C:\\Users\\Navigator\\Software\\Cicero-Word-Generator\\AtticusServer\\bin\\Debug\\")
sys.path.append("C:\\Users\\Navigator\\Software\\Cicero-Word-Generator\\WordGenerator\\bin\\Debug\\")

# from System.Reflection import Assembly
# Assembly.LoadFile("C:\\Users\\Navigator\\Software\\Cicero-Word-Generator\\AtticusServer.exe")
# Assembly.LoadFile("C:\\Users\\Navigator\\Software\\Cicero-Word-Generator\\WordGenerator.exe")

clr.AddReference("AtticusServer")
clr.AddReference("WordGenerator")



        