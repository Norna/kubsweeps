# 2016.02.08 RHS Original
# 
# ---------------------------------------------------

import configparser
import io
import os
import sys

class MetaDataBase(object):
    
    SECTION="DEFAULT"
    META_TEMPLATE="MetaTemplate.cfg"
    
    def __init__(self):
        
        # initialise memeber
        self._systemOptions=dict()
        self._options=dict()
        self._configParser=configparser.ConfigParser(allow_no_value=True)
        
        # read default template
        self.__readSystemOptions()
    
    def __readSystemOptions(self):
        
        fp = open(os.path.join(os.path.dirname(__file__), MetaDataBase.META_TEMPLATE));
        
        self._configParser.read_file(fp)
        for key,_ in self._configParser.items(MetaDataBase.SECTION):
            self._systemOptions[key]=""
            
    def Add(self,option,value):
        
        if not isinstance(option, str) or not option:
            raise ValueError("option must be a valid string")
        if not isinstance(value, str) or not value:
            raise ValueError("Value must be a valid string")
        
        if option in self._options:
            return
        
        self._options[option]=value
    
    def Set(self,option,value):
        
        if not isinstance(option, str) or not option:
            raise ValueError("option must be a valid string")
        if not isinstance(value, str) or not value:
            raise ValueError("Value must be a valid string")
        
        if option in self._systemOptions:
            self._systemOptions[option]=value
        elif option in self._options:
            self._options[option]=value
        else:
            raise KeyError("Unable to find the option!")
    
    def Get(self,option):
        
        if not isinstance(option, str) or not option:
            raise ValueError("option must be a valid string")
        
        if option in self._systemOptions:
            return self._systemOptions[option]
        elif option in self._options:
            return self._options[option]
        else:
            raise KeyError("Unknown option!")
    
    def Options(self):
        
        systemKeys = self._systemOptions.keys()
        customKeys = self._options.keys()
        
        return systemKeys + customKeys
            
        
        
    
        
        
        
        
        
        


