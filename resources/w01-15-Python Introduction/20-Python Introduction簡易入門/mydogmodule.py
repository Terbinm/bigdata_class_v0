class Dog:
    def __init__(self, name, age): #建構子
        self.name = name  #instance variabels實體變數 是public
        self.age = age
    def showMe(self):
         return "姓名:%s, age:%d(mydogmodule.py)" %(self.name, self.age)
    def __str__(self): #被print()列印時會執行此程式，等同於java的toString()
        return "姓名:%s, age:%d(mydogmodule.py)" %(self.name, self.age)

def hello():
    print('hello()方法來自mymodule.py--你懂得模組概念了!')