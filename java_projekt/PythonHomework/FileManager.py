import TBook as TB
class FileManager:
    FILE_PATH = "./java_projekt/PythonHomework/"
    FILE_NAME_EXPORT = "export.csv"
    @staticmethod
    def fileExport(self, phones: TB.TBook):
        result = ""
        for i in phones.bookentries:
            result = i.name +" "+ i.phone+" "+i.adress + " "+ i.gender + " " +i.email 
        with open (self.FILE_PATH + self.FILE_NAME_EXPORT, 'w') as file:
            file.write(result)
        print("Экспорт файла завершен")
        
    @staticmethod
    def ImportFile(self,phones: TB.TBook):
        with open(self.FILE_PATH + self.FILE_NAME_EXPORT, 'r') as data:
            phones.bookentries = data.readline()
        print("Import file finish")




