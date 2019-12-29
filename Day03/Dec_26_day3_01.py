#   날짜 : 12월 26일
#   작성자 : 윤찬우
#   프로그램 : 자료형, 문자열, 리스트 기본

import random as r

'''
#   ex1) str()
print("올해는"+str(2019)+"년 입니다.")

#   ex2) 실수 두개의 합을 구하는 예제
ex2a = 25
ex2b = 0.9
print("이제 나의 나이는 "+str(float(ex2a)+ex2b)+"살 먹은 건가?")

#   ex3) 변수에 봉인 이름 저장 후 4번 반복 출력
ex3name = "chanwoo"
print(ex3name*4)
for i in range(4):
    print(ex3name)

#   ex4) "파이썬 실습중입니다." 출력(특수문자)
print("\"파이썬 실습중입니다.\"")
print("'파이썬 실습중입니다.'")
print('"파이썬 실습중입니다."')

#   ex5) "파이썬 실습중입니다." 출력(특수문자)
print("파이썬\n실습중입니다.")

#   ex6) 변수에 국민대학교를 저장한 후 대학교만 추출
ex6name = "국민대학교"
print(ex6name[2:])
'''
#   ex7)
#   1. 빈 과일 리스트 생성
#   2. 좋아하는 과일 3개 추가
#   3. 첫번째 과일을 망고로 변경
#   4. 두번째과일과 세번째 과일 출력
#   5. 망고삭제
ex7fruits = []
ex7fruits.append("apple")
ex7fruits.append("grape")
ex7fruits.append("orange")
print(ex7fruits)
ex7fruits[0] = "mango"
print(ex7fruits)
print(ex7fruits[1:])
del(ex7fruits[0])
print(ex7fruits)


result = r.choice(ex7fruits)
print(result)
