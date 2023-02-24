import TBook as TB
import FileManager as FM
import Phonebook as PB


class Menu:     
    @staticmethod
    def mainMenu():
        while True:
            print("1 - Отобразить справочник\n"+
                "2 - Выгрузить данные \n"+
                "3 - Загрузить данные\n"+
                "4 - AddEntry\n"+
                "7 - search person\n"+
                "0 - EXIT")
            phones = TB.TBook() # объявил экземпляр Класса TBook
            
            
         
            choose = int(input("---->>>> ")) 
            run = FM.FileManager()
            if choose == 1:
                phones.showBook()
            elif choose == 2:
                
                run.fileExport(run, phones)
                print ("Export finish")
            elif choose == 3:
                
                run.ImportFile(run, phones)
                phones.showBook()
            elif choose == 4:
                
                fio = input(" Input FIO")
                phone=input("Input Phone")
                
                adress= input("Input adress")
                
                
                email= phones.getStringEmailValid()
                gender = input("Input gender")
                entry1 = PB.TBookentry(fio, phone,adress,email,gender)
                phones.addEntry(phones,entry1)# ??????????? 
                
            
                
                
            elif not choose != 0:
                break    
                    
            
            
         