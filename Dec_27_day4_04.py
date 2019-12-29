#   날짜 : 12월 27일_02
#   작성자 : 윤찬우
#   프로그램 : 터틀그래픽02

import turtle as t
import random as r

t.shape("turtle")
t.bgcolor("black")
t.color("white")
t.fillcolor("yellow")

t.begin_fill()
for i in range(8):
    t.lt(45)
    t.fd(50)
t.end_fill()

for i in range(5):
    print(r.randint(1, 45))

waitkey = t.textinput("","wait")
