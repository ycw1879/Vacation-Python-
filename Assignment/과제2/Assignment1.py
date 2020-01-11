#   날짜 : 01월 11일
#   작성자 : 윤찬우
#   프로그램 : Assignment2_01

#   1. 오륜기
import turtle as t

flags = [[-200, 100, 'red'], [0, 100, 'yellow'],[200, 100, 'green'],[-100, -100, 'blue'],[100, -100, 'purple']]
for x, y, c in flags:
    t.up()
    t.goto(x, y)
    t.down()
    t.color(c)
    t.begin_fill()
    t.circle(50)
    t.end_fill()
