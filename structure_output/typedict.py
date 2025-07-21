from typing import TypedDict

class Person(TypedDict):
    name:str
    age:int

new_person:Person = {'name':'harshil','age':21}
new_person1:Person = {'name':'harshil','age':'21'}
print(new_person)