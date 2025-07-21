from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name:str='hp'
    age:Optional[int]=None
    email:EmailStr
    cgpa:float=Field(gt=0,lt=10,default=7,description="It represents a value that is result of all semester accumulated")

#description will also be passed to the llm


#p={'name':'harshil'}
#p={'age':21}
p={'email':'ab@gmail.com','cgpa':9.33}
student=Student(**p)

#print(type(student))
print(student)

student_json=student.model_dump_json()
print(student_json)