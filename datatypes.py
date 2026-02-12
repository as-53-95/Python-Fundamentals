age = 17 #integer
temperature = 36.54 #float
greeting = "hey" #string
is_married = True #boolean

print("I am",age,"years old")
print("The current body temperature of our patient is",temperature,"degrees celcius")
print(greeting,"Asher")
print("Are you married?",is_married)

#A datastructure refers to multiple values stored in a single variable
#they include, lists, tuples, dictionaries, sets and arrays

cars = ["Toyota","Mercedes", "BMW"] #list-Ordered and changeable. Carries different data-types.
fruits = ("Banana","Mango","Grape","Avocado") #tuple-ordered and unchangeable
countries = {"Italy","France","Kenya","Taiwan"} #set-unordered and unchangeable
Student = {
    "name" : "Asher Wafula",
    "age" : 17,
    "gender" : "Male",
    "course" : "FullStack"
} #dictionary
languages = ["Python","Java","C++"] #Array- Ordered list that is unchangeable. It carries similar data-types

print(cars)
print(fruits)
print(countries)
print(Student)
print(Student["name"])

#Typecasting is the process of converting variables from one data type to another using built in functions.

print(int(temperature))

#end of typecasting

