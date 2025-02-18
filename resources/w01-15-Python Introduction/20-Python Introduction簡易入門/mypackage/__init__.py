print('當你import這個目錄時，__init__.py被呼叫了')

from .mymodule import Dog

# 這樣寫雖也可以，但不建議，只適用於執行路徑是與mypackage相同目錄下。
# from mypackage.mymodule import Dog

#from mymodule import Dog #若缺少一點不能運作

dog = Dog('doggy',5)

dogshow = dog.showMe