fruits=["apple", "banana", "cherry"]
for i in range(3):
    print(fruits[i])




subjects = ["Math", "Science", "History", "English"]
append_result = subjects.append("Art")  # Appends "Art" to the list
print(subjects)  # Output: ['Math', 'Science', 'History', 'English', 'Art']




numbers = [1, 2, 3, 4, 5]

print(numbers)  # Output: [1, 2, 3, 4, 5]

numbers.pop()  # Removes and returns the last item (5)
print("By use of pop() method it removes the last value:", numbers)  # Output: [1, 2, 3, 4]


numbers.remove(2)  # Removes the first occurrence of 2
print("By use of remove() method it removes the value 2:", numbers)  # Output: [1, 3, 4]

numbers.clear()  # Removes all items from the list
print("By use of clear() method it removes all the values in the list:", numbers)


numbers.extend([6, 7, 8])  # Extends the list by appending elements from the iterable
print("By use of extend() method it adds the values 6,7,8 in    the list:", numbers)  # Output: [6, 7, 8]


student_name = ["John Doe", "Jane Smith", "Alice Johnson", "Bob Brown", "Charlie Davis"]
# print(type(student_name))  # Output: <class 'list'>
print(student_name)  # Output: ['John Doe', 'Jane Smith', 'Alice Johnson', 'Bob Brown', 'Charlie Davis']
print(f"First three students in {student_name} are follows:", student_name[0:3])
  # Output: ['John Doe', 'Jane Smith', 'Alice Johnson'] (accessing the first three elements of the list)

# negative indexing
print(f"Last student in {student_name} is:", student_name[-1])

# slicing with step
print(f"Every second student in {student_name} is:", student_name[::2])  # Output: ['John Doe', 'Alice Johnson', 'Charlie Davis'] (accessing every second element of the list)


# Assigning a new value to an existing index
student_name[1] = "Samiullah"
print(f"After changing the second student name in {student_name} is:", student_name)  # Output: ['John Doe', 'Samiullah', 'Alice Johnson', 'Bob Brown', 'Charlie Davis'] (changing the second element of the list)

# appending a new value to the list
student_name.append("David Wilson")
print(f"After appending a new student in {student_name} is:", student_name)  # Output: ['John Doe', 'Samiullah', 'Alice Johnson', 'Bob Brown', 'Charlie Davis', 'David Wilson'] (appending a new element to the list)

# popping the last value from the list
student_name.pop()
print(f"After popping the last student in {student_name} is:", student_name)


# removing a specific value from the list
student_name.remove("Samiullah")
print(f"After removing the second student name in {student_name} is:", student_name)  # Output: ['John Doe', 'Alice Johnson', 'Bob Brown', 'Charlie Davis'] (removing a specific element from the list)


# for clearing the list
student_name.clear()
print("After clearing the list  is:", student_name)  # Output: [] (clearing all elements from the list)