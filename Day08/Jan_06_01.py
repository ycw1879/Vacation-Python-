#   날짜 : 1월 6일_01
#   작성자 : 윤찬우
#   프로그램 : 함수2
'''
#   ex1) 지역변수, 전역변수
def a():
    test = 30 # 지역 변수
    print(test) # 지역변수 출력

def b():
    print(test) # 전역변수 출력
        
test = 100 # 전역변수
a()
b()

#   ex2) global 키워드
def a():
    global test # 전역변수로 설정
    test = 30 # 지역 변수
    print(test) # 지역변수 출력

def b():
    print(test) # 전역변수 출력
        
test = 100 # 전역변수
a()
b()

#   ex3) 디폴트 인수
#   계절학기 정보(이름, 과목명)를 출력하는 함수.(과목명 = "과소사")
def Vacation_Lecture(_name, _subject = "과소사"):
    print("저의 이름은 %s입니다. %s를 수강중입니다." %(_name, _subject))
Vacation_Lecture("윤찬우")

#   ex4) 키워드 인수
def Sum(a, b, c):
    return a + b + c

print(Sum(c = 50, a = 40, b = 30))

#   ex5) pass 키워드
#   계절학기 성적을 처리하는 함수의 이름만 설정하고 나중에 삽입할 경우
def Score():
    pass
'''
#===============================================================
#   ex6) 반환 값이 없는 경우 (인수X, 매개변수 X)
def Practice():
    pass

#   ex7) 출력하는 함수 (인수 1개, 매개변수 1개)
def Practice1(_blog):
    print(_blog)
Practice1("김민재 : 점수가 이상하네")
    
#   ex8) 반환하는 함수 (인수 2개, 매개변수 2개)
def Practice2(_k, _v):
    return _k,_v
k, v = Practice2('김민재 :', "점수가 이상하네")
print(k, v)

#   ex9) 출력하는 함수 (인수 2개, 매개변수 2개), 값을 입력받는다.
def Practice3(_k, _v):
    print(_k, _v)
Practice3('김민재 :', "점수가 이상하네")

#   ex10) 출력하는 함수 (인수 3개, 매개변수 3개), 디폴트 인수 적용
def Practice4(_k, _v, _v2 = 30):
    return _k, _v, _v2
k, v, v2 = Practice4('김민재 :', "(크흡;;)", "점수가 이상하네")
print(k, v, v2)
