class Hero:

    __jumlah = 0;

    def __init__(self,name):
        self.__name = name
        Hero.__jumlah += 1

    def getjumlah(self):
        return Hero.__jumlah

    def getjumlah1():
        return Hero.__jumlah

    @staticmethod
    def getjumlah2():
        return Hero.__jumlah
    
    @classmethod
    def getjumlah3(cls):
        return cls.__jumlah

omloh = Hero('omloh')
print(Hero.getjumlah2())
senoy = Hero('senoy')
print(omloh.getjumlah2())
nunun = Hero('nunun')
print(omloh.getjumlah3())