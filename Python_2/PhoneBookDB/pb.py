import sys
from contact import Contact
class Phonebook:
   
   #Method (Contructor)
   def __init__(self):
      self._entries = [] #private field named entries

   #Method (Mutator)
   def add_entry(self, name, number):
      contact = Contact(name, number)
      self._entries.append([contact])
   
   #Method (Accesor/Query)
   def lookup(self, name):
      for contact in self._entries:
         if contact.get_name() == name:
           return contact.get_number()
      return "Private Number"

   #Method (Accessor/Query)
   def reverse_lookup(self, number):
      for contact in self._entries:
         if contact.get_number() == number:
           return contact.get_name()
      return "Unknown"

   #Method (Accessor/Query)
   def size(self):
      return len(self._entries)
   
   #Special Method
   def __str__(self):
      s = ''
      for contact in self._entries:
         s += contact.get_name() + ' ' + contact.get_number() + "\n"
      return s
   


def main(argv):
   pb = Phonebook() #calls Phonebook.__init__
   pb.add_entry("Alexander Thompson", "245-444-4444")
   print(pb, end='')
   print(str(pb), end='')
   print(pb.lookup("Alexander Thompson"))
   print(pb.reverse_lookup("245-444-4444"))
   return 0

if __name__=='__main__':
   sys.exit(main(sys.argv))
