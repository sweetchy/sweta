'''import class4

print(class4.name)
print(class4.age)'''


'''from class4 import *
print(name)
print(age)
print(place)'''

'''import datetime as dt
import time
print(dt.date.today())
print('format time:',time.asctime())'''

'''import webbrowser
a=input("search video")
print("opening browser")
webbrowser.open_new_tab('http://youtube.com/search?q=%s'%a)'''



'''import os
print('my current working directory:',os.getcwd())'''

'''import math
num=(int(input('enter a number')))
print('factorial:',math.factorial(num))'''

from termcolor import colored

print (colored('my name is','yellow','on_grey'),colored('sweta','green','on_red'))

text=colored('color look nice!!!','blue',attrs=['reverse','blink'])
print(text)