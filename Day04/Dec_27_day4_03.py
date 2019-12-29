#   날짜 : 12월 27일_03
#   작성자 : 윤찬우
#   프로그램 : 터틀그래픽

import turtle as t
import random as r

s = t.Screen() # 이미지 설정 개체
s.bgpic("pic.png") # BackGroud PICture

img1 = "myung.gif"
img2 = "sung.gif"

s.addshape(img1)
s.addshape(img2)

#----------------------등록완료

t1 = t.Turtle()
t2 = t.Turtle()

t1.shape(img1)
t2.shape(img2)

t1.up()
t2.up()

t1.goto(300,200)
t2.goto(300,-200)

t1.down()
t2.down()

for i in range(30):
    t1.fd(r.randint(-40, 20)*2)
    t2.fd(r.randint(-40, 20)*2)

waitkey = t.textinput("", "wait")
