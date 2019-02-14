#program to print if the year is leap or not
'''year = int(input("Enter the year : "))
if year% 4 == 0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

#progran to print multiplication table intered by the user
a = int(input("Enter number for which the table is required : "))

for i in range(1,11):
    print(a ,"*", i, "=", a*i )'''

#program to add 10 numbers using only one input statement add them to list
'''list = []
i=1
while i <=10:
    a = input("Enter #" + str(i))
    if a.isnumeric():
        list.append(a)
        i = i+1
    else:
        print(a, "is not in list")
    print("List of numbers = ", list)'''


## program to create a form
name = input("Enter your name : ")
age = input("Enter your age : ")
mob_num = input("Enter mobile number : ")

while True:
    if name =="":
        name = input("Name cannot be empty, enter your name again : ")
    elif name.isalpha() == False:
        name = input("Name can contain only alphabets, enter your name again : ")
    else:
        if age =="":
            age= input("age cannot be empty, enter your age again : ")
        elif age.isdigit() == False:
            age = input("Age can contain only numbers, enter your age again : ")
        elif int(age) < 19:
            age = input("Age can only be over 18, enter your age again : ")
        else:
            if mob_num =="":
                mob_num = input("Mobile number cannot be empty, enter your number again : ")
            elif mob_num.isdigit() == False:
                mob_num = input("Mobile Number can contain only numbers, enter your number again : ")
            else:
                print("Name = ", name , "\nAge = ", age, "\nMobile Number = ", mob_num)
                break

#list of the list
list = [23, 11, 69, 12, 34, 2, 6, 23, 43, 1233, 23, 222, 69, 23]
print("list is ", list)

a = int(input("Enter number to be removed"))

for x in list:
    if x == a:
        list.remove(x)
print("new list is", list)

