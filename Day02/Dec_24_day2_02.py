#   날짜 : 12월 24일
#   작성자 : 윤찬우
#   프로그램 : 변수와 연산자
'''
print('12/24')

print()함수 형식

#   1. 문자열 출력
print("출력할 문자열")

#   2. 변수에 저장된 값 출력
print(변수명)

#   3. 변수 + 문자열 혼합 출력
print(변수, '문자열')


#   ex1) 변수 생성 및 출력
#   이름을 저장하는 변수 생성 후 이름 출력

#   변수명 = 값


name = '윤찬우'
print(name)

#   본인의 혈액형을 저장하는 변수 생성 후 혈액형 출력
blood = 'A'
print(blood)

#   학년을 저장하는 변수 생성 후 학년 출력
degree = 3
print(degree)

#   ex2) 나이를 저장하는 변수 생성후 출력
#   출력 : 당신은 ??살입니다.
age = 25
print('당신은',age,'살입니다.')

#   ex3) 이름을 저장하는 변수 생성, 나이를 저장하는 변수 생성 후 출력
#   출력 : ??님은 ??살입니다.
name = 'chanwoo'
age = 25
print(name+'님은',age,'살입니다.')


### 터틀 그래픽 ###

import turtle as t
#   import 모듈 : 해당 모듈을 불러온다.
#   as t : turtle모듈이름을 t라는 별칭(약자)를 사용한다.
t.shape('turtle')       #   동물의 종류 turtle

radius = 50             #   반지름의 크기
t.color('red')          #   거북이 색
t.circle(radius)        #   원을 그려주는 함수
t.fd(100)               #   전진

#   ex5) 이름을 입력받아 출력하는 프로그램

변수명 = input("문자열")


name = input("당신의 이름은?")
print('당신의 이름은',name,'입니다.')

#   ex6) 학교와 확과를 입력받아 출력하는 프로그램
#   출력 : ???대학교 ???학과 입니다.
univ = input('학교 : ')
dep = input('학과 : ')
print(univ+'대학교',dep+'학과 입니다.')

#   ex7) 이름과 나이를 입력받아 출력(???님은 ??살입니다.)
name = input("이름 : ")
age = input("나이 : ")
print(name+'님은',age+'살입니다.')

#   ex8) 두 정수를 입력받아 곱을 구하는 프로그램
#   출력 : ?X? = ??
x1 = int(input('피연산자1 : '))
x2 = int(input('피연산자2 : '))
print(x1, 'X', x2, '=', x1 * x2)

#   ex9) 산술 연산자
#   정수 두개를 입력 받아 사칙연산, 나머지 연산 결과 출력
a = int(input('정수입력1 : '))
b = int(input('정수입력2 : '))

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)


#   ex10) 관계 연산자
a = int(input('정수입력1 : '))
b = int(input('정수입력2 : '))

print(a>b)
print(a>=b)
print(a<=b)
print(a<b)
print(a==b)
print(a!=b)

#   ex11) 논리 연산자
a = 50
b = 30

print(a==50 and b==30)
print(a==50 and b==10)

print(a==40 and b==30)
print(a==20 and b==10)

print(not a==20)
print(not b==30)
'''
