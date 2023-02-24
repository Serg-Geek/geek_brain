
import enum

from typing import Any


class TBookentry:
 

    def __init__ (self, name,  phone, adress, email, gender):
        self.name = name
        
        self.gender = gender
        self.phone = phone
        self.email = email
        self.adress = adress


    def getName (self):
        return self.name
    
    
    def getPhone(self):
        return self.phone
    
    def getAdress(self):
        return self.adress
    
    def getEmail(self):
        return self.email 
    
    def getGender(self):
        return self.gender
    
  
    

 

