# print("Hello, World!")

# a = input()
# b = input()
# separator = input()[0]
# print(a, b)
# print(a, b, end="")
# print(a, separator, b, sep='  ')
# print(a, b, sep='')

# i=0
# j=0
# for i in range(0, int(a)):
#   print(a, end="")
#   i = i+1
# while (j < int(b)):
#   print(b, end="")
#   j = j+1

# #loops continue and break

# for i in 'geeksforgeeks':
#     if i == 'e' or i == 's':
#         continue
#     print('Current Letter :', i)

# for letter in 'geeksforgeeks':
#     if letter == 'e' or letter == 's':
#         break
# print('Current Letter :', letter)

# for letter in 'geeksforgeeks':
#     continue
# print('Last Letter :', letter)


# # Assigning value to variable

# x = 10                          
# x = "Now a string"
# print(x) 

# del x                           # Removing the variable using del

# a = b = c = 100
# print(a, b, c)


# # Define variables with different data types
# n = 42
# f = 3.14
# s = "Hello, World!"
# li = [1, 2, 3]
# d = {'key': 'value'}
# bool = True

# # Get and print the type of each variable
# print(type(n))   
# print(type(f)) 
# print(type(s))   
# print(type(li))     
# print(type(d))     
# print(type(bool))

# word = "Python"
# length = len(word)
# print(length)


# n = int(input())
# k = 0
# for i in range(1, n+1):
#     k = k+i
# print(k)



# ## Mathmatical operators
# a = 15
# b = 4
# print("Floor Division:", a // b)                # Floor Division
# print("Modulus:", a % b)                        # Modulus
# print("Exponentiation:", a ** b)                # Exponentiation
# print(a > b)
# print(a < b)
# print(a == b)
# print(a != b)
# print(a >= b)
# print(a <= b)

# b += a   #b = a+b
# b -= a    #b=a-b
# b *= a


# ## Boolean operators
# a = True
# b = False
# print(a and b)
# print(a or b)
# print(not a)


# ## Ternary opeartor 
# a, b = 10, 20
# min = a if a < b else b
# print(min)



# #keywords in Python

# x = 20
# list = [10, 20, 30, 40, 50]
# if (x not in list):                                         #not in
#     print("x is NOT present in given list")
# else:
#     print("x is present in given list")

# a = 5
# b = 5
# print(b == 5)
# print(a == 8)
# print(False == 0)
# print(True == 1)
# print(True + True + True)
# print(True + False + False)  
# print(3 in [1,2,3]) 
# print(2 is 2)

# a = [1, 2, 3]
# b = a
# c = [1, 2, 3]
# print(a is b)  # True: a and b refer to the same object
# print(a is c)  # False: a and c have same value but are different objects


# #Lambda keyword is used to make inline returning functions with no statements allowed internally. 
# k = int(input())
# g = lambda k: k*k
# print(g(k))


# #list
# a = ["Geeks", "For", "Geeks"]
# print("Accessing element from the list")
# print(a[0])
# print(a[2])

# print("Accessing element using negative indexing")  # negative indexing starts with -1
# print(a[-1]) 
# print(a[-3])

##Nested functions
def calling(x):
    print(x)
    def nested1():
        print("you are in nested!")
    nested1()
    def nested2():
        nested1()
    nested2()
calling(5)

## recursive function
def factorial(n):
    if n == 2: 
        return 2
    else:
        return n * factorial(n-1)
print(factorial(5))


## Pass by value and pass by ref -> in Python nothing 
## since everything is an object still
def update(x):
    x = 10      ##ref to a lst is not broken
    print(x) 
def update2(x):
    x[1] = 10      ##ref is broken to a and new ref is created for x
    print(x) 

a = 5
update(a)
print(a)
update(5)

lst = [1, 2, 3]
update(lst)
print(lst)
update2(lst)
print(lst)

print(lst[0])
lst.append(4)                     #adds one element at the end
print(lst)
lst.sort()                        #sort in ascending order
print(lst)
lst.sort(reverse=True)            #sort in descending order
print(lst)
lst.reverse()                      #reverse list
print(lst)
lst.insert(0, "hi")               #insert an element at index
print(lst)

tup = (1,2,3,3,3,2,2,)
print(tup)
#tup[3] = 4                        ##tuples are immutable
print(tup.index(1))
print(tup.count(2))


## Dictionary

info = {
    "name": "nish",
    "comp": "zscaler",
    "loc": "mohali",
    "age": 26,
    "skills": ["devops", "python"],
    "is_adult": True,
    "subjects": {
        "phy": 98,
        "chem": 90,
        "math": 100
    }
}

print(info["name"])
info["surname"] = "garg"
print(info)

null_dict = {}
print(null_dict)
print(info["subjects"]["phy"])

new_dict = {"name": "mayank", "age": 27}
info.update(new_dict)
print(info)


set1 = {1,4,5,"hello",5,5}
print(type(set1))
print(set1)
print(len(set1))
set2 = set()
set2.add(2)
print(set2)
set1.add("world")
set1.add((9,2,4))
print(set1)                      #cant add list in a set because its unhashable
set3 = set1.union(set2)
set4 = set1.intersection(set2)
print(set3)
print(set4)
print(set1)
print(set2)
set2.remove(2)
print(set2)
set1.clear()
print(set1)  