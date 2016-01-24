import sys

class Contact:
   
   def __init__(self, name, number):
      self._name = name
      self._number = str(number)

   def get_name(self):
      return self._name

   def set_name(self, name):
      self._name = name
      
   def get_number(self):
      return self._number
    

   def set_number(self, number):
      self._number = str(number)
     
    








