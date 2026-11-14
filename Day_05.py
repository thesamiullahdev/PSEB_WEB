# Variables

'''
Rules for Python variables:

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
'''

# _username = "John"  # string variable
# username  = "John"  # string variable
# user_name = "John"  # valid variable name, underscore is allowed

# int = 10  # integer variable
# float = 10.5  # float variable


myName = 'Samiullah'
print(myName)
my_id =265428
print(my_id)
roll_no ='F23BSEEN1M01202' 
print (roll_no)
my_profession = "sowftware Engineer"
print (my_profession)



first_name= "Rizwan"
last_name= "Ulo ka patha"
print("full_name : ", first_name +" "+ last_name)

b = 4 
c = 5
a = b+c

print(a)


B = 'Rizwan' 
H = 'Mohsin'
X = (B+H)

print(X)

import random

Students = ["asad" , "nouman" , "Rizwan " , "samiullah"]
random_name = random.choice(Students)
print (random_name)



student_name = "Usman Ghazi"

print(student_name.upper())

print(student_name.lower())

print(student_name.capitalize())

print(student_name.title())

print(student_name.strip())

print(student_name.replace('Usman','Orhan'))


print(student_name.split("n"))


print(student_name.join('Usman'))

print(student_name.join('M'))

list =('students' , 'teachers' , 'staff') 

print((" ") , "hello" , " ".join(list) )

print(student_name.find("azi"))

print(student_name.count("a"))

print(student_name.isdigit())

print(student_name.isalpha())