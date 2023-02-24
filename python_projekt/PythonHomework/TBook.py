import re
import Phonebook as PB
class TBook:
   

   
    
    # def __init__(self) -> None:
    bookentries = []
    @staticmethod
    def  addEntry(self,Bookentry: PB.TBookentry):
        self.bookentries.append(Bookentry)
        
    def searchEntry(self):
        name = input("input Name")
        for i in self.bookentries:
            if i.name  == name:
                print(i.name + " " + i.phone +" "+ i.adress + " "+ i.gender + " " +i.email )
            else: print(" not found ")   
    
    # получение почты с валидацией
    @staticmethod
    def getStringEmailValid():
        while(True):
                
            email = input("Input EMAIL (в формате *******@****.**)")
            pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"
            if email == "":
                return email
            if re.match(pattern, email) is not None:
                return email
            else:
                print("Введите email в верном формате")
                return email

    def showBook(self):
        for i in self.bookentries:
            print(i)
            print()  
  