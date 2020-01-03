#   날짜 : 1월 3일_01
#   작성자 : 윤찬우
#   프로그램 : 함수1

'''
====함수 정의====
def 함수명():
    진행문장
    
====함수 호출====
함수명()

#   ex1) 학과와 이름 정보를 출력하는 함수
def info():
    print("컴퓨터공학")
    print("윤찬우")

info()

=====값을 반환하는 함수 형식=====
def 함수명(매개변수):
    return 결과값
    
1) print(함수명(인수))
2) 변수명 = 함수명(인수)
    print(변수명)
===========================

=====값을 출력하는 함수 형식=====
def 함수명(매개변수):
    실행문장
함수이름(인수)
===========================

#   ex2) 5의 제곱을 출력하는 함수
def sq(num):
    print(num * num)
sq(5)

#   ex3) 5의 제곱을 반환하는 함수
def sq(num):
    return num * num
print(sq(5))

#   ex4) 입력한 정수의 제곱을 출력하는 함수
def sq(num):
    print(num * num)
sq(int(input("정수 입력 : ")))

#   ex5) 입력한 정수의 제곱을 반환하는 함수
def sq(num):
    return num * num
sq(int(input("정수 입력 : ")))

#   ex6) 두 정수의 합을 출력하는 함수
def twosum(x1, x2):
    print(x1 + x2)

#   ex7) 정수 하나를 입력받아 1부터 입력한 정수까지의 합을 반환하는 함수
def retint():
    sum = 0
    ll = int(input("정수 입력 : "))
    for i in range(1, ll+1):
        sum += i
    return sum
print(retint())

#   ex8) 이름과 나이를 입력 받아 출력하는 함수
def information():
    name = input("이름 : ")
    age = input("나이 : ")
    print("이름은 %s이고 나이는 %s입니다." %(name, age))
information()

#   ex8) 반지름을 입력 받아 원을 그리는 함수 작성
#   (-200, 0), (0, 0), (200, 0)위치에 원을 그리는 함수
import turtle as t

t.color("red")

def radius(r):
    t.up()
    t.goto(-200, 0)
    t.down()
    t.circle(r)
    t.up()
    t.goto(200, 0)
    t.down()
    t.circle(r)
    t.up()
    t.goto(0, 0)
    t.down()
    t.circle(r)

length = int(t.textinput("","반지름 입력 : "))
radius(length)
'''
#=================================여기서부터는 실습 예제
#   ex10) 실수 두개를 입력 받아 합을 반환하는 함수
def twosum(a, b):
    return a + b
print(twosum(float(input("정수 입력1 : ")), float(input("정수 입력1 : "))))


#   ex11) 단을 입력 받아 해당 구구단을 출력하는 함수
def multi(n):
    for i in range(1, 10):
        print("%d X %d = %d" %(n, i, n * i))
multi(int(input("단 입력 : ")))

#   ex12) 변의 길이의 입력 받아 별을 그리는 함수
#   (0, 200), (0, -200) 위치에 별을 그린다.
import turtle as t

t.color("red")
def star(l):
    t.up()
    t.goto(-200, 0)
    t.down()
    for i in range(5):
        t.fd(l)
        t.lt(144)
    t.up()
    t.goto(200, 0)
    t.down()
    for i in range(5):
        t.fd(l)
        t.lt(144)
star(int(t.textinput("","길이 입력 : ")))

#   ex13) 세 정수의 곱을 출력하는 함수
def mux(x1, x2, x3):
    print(x1 * x2 * x3)
mux(1, 2, 3)
