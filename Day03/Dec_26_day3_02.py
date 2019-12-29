#   날짜 : 12월 26일
#   작성자 : 윤찬우
#   프로그램 : 실습

#   1번
x1 = int(input("정수입력1 : "))
x2 = int(input("정수입력2 : "))
print(str(x1)+"과 "+str(x2)+"의 곱은 "+str(x1 * x2)+"입니다.")

#   2번
name = input("이름 입력 : ")
real = input("실수 입력 : ")
print(name+"님의 키는", str(real)+"cm입니다.")

#   3번
print('"오늘은 12월 26일입니다."')

#   4번
arr = []
print(arr)

arr.append("국어")
arr.append("영어")
arr.append("수학")
arr.append("과학")
print(arr)

arr[3] = "파이썬"
print(arr)

del(arr[0])
print(arr)

#   5번
import random as r
list = ["한식","중식","양식"]
select = r.choice(list)
print(select)
