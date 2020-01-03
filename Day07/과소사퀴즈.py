'''
#Q1
name=input("이름:")
age=int(input("나이:"))
print(name+"님은 "+ str(age)+"살입니다.")



#02
num1=float(input("실수 입력:"))
num2=float(input("실수 입력:"))
print(num1,"+",num2,"=",num1+num2)


#Q3
import turtle as t
radius=t.textinput("","반지름 입력:")
area=3.14*float(radius)*float(radius)
t.write("원의 면적은"+str(area)+"입니다.")


#Q4
seasons=[]
seasons.append("봄")
seasons.append("여름")
seasons.append("가을")
seasons.append("겨울")
del(seasons[2])
print(seasons)
'''

#Q5

import turtle as t
t.shape("turtle")
t.bgcolor("green")
t.speed(0)
t.color("blue")
t.begin_fill()
for i in range(5):
    t.fd(100)
    t.lt(72)
t.end_fill()
t.ht()
































