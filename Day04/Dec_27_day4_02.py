#   날짜 : 12월 27일_02
#   작성자 : 윤찬우
#   프로그램 : 터틀그래픽02

import turtle as t
import random as r

t.bgcolor("black")
t1 = t.Turtle()
t2 = t.Turtle()

t1.shape("turtle")
t2.shape("turtle")

t1.color("white")
t2.color("green")

t1.shapesize(3)             # 거북이 사이즈
t2.shapesize(3)

t1.up()
t2.up()

t1.goto(300,200)
t2.goto(300,-200)
t1.lt(180)
t2.lt(180)

t1.down()
t2.down()

#   for문 (반복문) 형식
'''
for 변수명 in range(반복횟수):
    반복문장
'''
for i in range(30):
    t1.fd(r.randint(-20, 60))
    t2.fd(r.randint(-20, 60))

#   ranint(시작값, 마지막값)
#   e)r.randomint(1, 45) 1부터 45까지 랜덤 숫자

name = t.textinput("", "대기")
