from enum import Enum
from MetaData.MetaDataBase import *

class ServiceType(Enum):
    SearchEngine=0
    ObjectiveFunction=1
    Storage=2

class ServiceBase(object):
    
    def __init__(self,urlCorrdinator):
        self.__urlCorrdinator = urlCorrdinator
        
    
    def Register(self):
        pass 
    
    def GetMetaData(self):
        pass
        
