#!/usr/bin/python3
# -*- coding: utf-8 -*-


class Phonebook:
  '''A Phonebook class.'''
  
  phone_list = []
  person_list = []
  
  def __init__(self, phone=None, person=None):
    self.phone =  phone
    self.person = person
    if phone != None:
      if type(phone) == type(1):
        self.phone_list.append(phone)
      else:
        new_phone = []
        for i in phone:
          if i in '0123456789':
            new_phone.append(i)
        self.phone_list.append(int(''.join(new_phone)))
      self.person_list.append(person)
    

class Person:
  '''A Person class'''
  
  person_list = []
  
  def __init__(self, phonebook):
    for item in phonebook.person_list:
      if item not in self.person_list:
        self.person_list.append(item)
      else:
        pass
  
  def get_phones(self, phonebook, name):
    '''Method for getting phones for name from phonebook.'''
    phones_for_name = []
    for i in range(len(phonebook.phone_list)):
      if phonebook.person_list[i] == name:
        phones_for_name.append(phonebook.phone_list[i])
    return phones_for_name

    
  def get_names(self, phonebook, phone):
    '''Method for getting person names for phone from phonebook.'''
    names_for_phone = []
    for i in range(len(phonebook.person_list)):
      if phonebook.phone_list[i] == phone:
        names_for_phone.append(phonebook.person_list[i])
    return names_for_phone

    
  def get_phones_by_person(self, phonebook):
    '''Method for creating table of person with their phone's numbers.'''
    list_of_persons = set()
    list_of_persons.update(phonebook.person_list)
    phonebook_by_person = []
    for i in sorted(list_of_persons):
      phonebook_by_person.append([i, self.get_phones(phonebook, i)])
    
    return phonebook_by_person
    
  
  def get_names_by_phone(self, phonebook):
    '''Method for creating table of phones with their owners.'''
    list_of_phones = set()
    list_of_phones.update(phonebook.phone_list)
    phonebook_by_phone = []
    for i in sorted(list_of_phones):
      phonebook_by_phone.append([i, self.get_names(phonebook, i)])
    
    return phonebook_by_phone

class Manager(Person):
  """docstring for Manager"""
  def __init__(self, grade):
    super(Person, self).__init__()
    self.grade = grade
    
  
if __name__ == '__main__':
  phones_and_ABC = [[37615, 'Max'], [710434, 'Max'], [36683, 'Valera'], [36366, 'Khadin'], ['+7 (985) 181-72-75', 'Khadin'], [25007, 'Ershov'], [25007, 'GD']]
  for i in phones_and_ABC:
    pb1 = Phonebook(i[0], i[1])
  
  print(pb1.phone_list, '\n', pb1.person_list)
  person = Manager(pb1)
  print(person.person_list)
  person.grade=5
  print(person.grade)
  
  for i in person.get_phones_by_person(pb1):
    print(i)
  for i in person.get_names_by_phone(pb1):
    print(i)
  