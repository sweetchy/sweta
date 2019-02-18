#f=open('File.txt','w')
#f.writelines('THis is my \n first file')
#f.close()#

#with open("file.txt","r")as f:
    #text=f.read()
    #print(text)

    #code to append text
#f=open('file.txt','a')
#f.writelines("\njhgjyjfhfhfhg")
#f# .close()

#to write to a file until i want to
'''f12=open("file2.text",'w')
text=input("write to the  file.........write quit to stop")
while text!='quit':
    f12.writelines(text+'\n')
    text=input()
print("done with writing now saving")
f12.close()'''

'''try:
    a=int(input('enter first a number'))
    b=int(input('enter second number'))
    div=a/b
    print("the result is",div)
except ZeroDivisionError:
    print("you can not divide by zero")
except:
    print("some problem occured")'''
#for error
'''class LowAgeError(Exception):
    def __init__(self):
        super(LowAgeError,self).__init__("age should be greater than 18")
age=int(input("enter the age"))
if age<18:
    raise LowAgeError
else:
    print("accepted")'''

lst_com=[x for x in range(25)]
gen_exp=(x for x in range(20))
print("list comprehension>>>",lst_com)
print("generator Expression>>>",gen_exp)
for x in gen_exp:
    print(x)










