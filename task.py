#Question 1
#Shopping Cart Example

shopping_cart = ["shirts","shoes","pents","jackets","caps"]

#for appending new product in the list
append_result = shopping_cart.append("socks")
print("Result:",shopping_cart)

#insert at 1

shopping_cart.insert(1,"glasses")
print("Result:",shopping_cart)

#pop

poped_item = shopping_cart.pop()
print(shopping_cart)
print(poped_item)

#Remove

Removed_item = shopping_cart.remove("shoes")
print(shopping_cart)

print(shopping_cart[0:len(shopping_cart):2])


#Question 2

a=[20,45,32,65,86,94,43]
b=a 
c=a.copy()
print(a)
print(b)
print(c)

#After Uupdating a

a=[43,23,53,64,76]
print(a)
print(b)
print(c)

#Question 3

Table_of_seven =list(range(1,71))
print(Table_of_seven)
print("Table of Seven: ", Table_of_seven[6::7])

#Question 4

student_record = (("ahsan",1,54),("asad",2,63),("usman",3,65))
student_name, student_rolno, student_marks =student_record[0]
print(student_name)
print(student_rolno)
print(student_marks)

student_name, student_rolno, student_marks =student_record[1]
print(student_name)
print(student_rolno)
print(student_marks)
