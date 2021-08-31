
#class that uses the protected function
class Protected: 
 
 
    def __init__(self):
        self._protectedVar = 0

#object that uses the protected funtion

obj = Protected()
obj._protectedVar = 34
print(obj._protectedVar)

#class that uses the private function
class Protected:
    def __init__(self):
        self.__privateVar = 12
    
    def getPrivate(self):
        print(self.__privateVar)
    
    def setPrivate(self, private):
        self.__privateVar = private

#object that uses the private funtion

obj = Protected()
obj.getPrivate()
obj.setPrivate(23)
obj.getPrivate()
