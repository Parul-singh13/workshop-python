#class Dog:
    #def __init__(self,name ):
      #self.name=name
#Dog1=Dog("tom") 
#print(Dog1.name)     
class Car:
    def __init__(self,make,model):
     self.make=make
     self.model=model
car1=Car("Toyota","Camry")  
car2=Car("honda","civic")   
print(car1.make,car1.model)
class BankAccount:
   def __init__(self,accountno,balance):
      self._accountno= accountno
      self._balance=balance
   def get_balance(self):
      return self._balance
acount1=BankAccount("12345",1000)  
print(acount1._accountno) 
print(acount1.get_balance())
   


   