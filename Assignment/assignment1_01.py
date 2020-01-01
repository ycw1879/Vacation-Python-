#   날짜 : 1월 1일
#   작성자 : 윤찬우
#   프로그램 : 과제1_01(조건문 사용)

#   Step 1) 상품 목록을 출력한다.
item = [["Cabbage", 5000],["Daikon", 2000],["Lettuce", 3000]]
print("-------=== I T E M ===-------")
for i in range(3):
    print(str(i + 1) + '.', item[i][0], "\tprice =", item[i][1])

#   Step 2) 고객이 고른 상품 번호를 입력 받는다. [1 ~ 3, 예외 사항은 고려하지 않는다.]
choice = int(input("Select Item [1 ~ 3] ? = \n")) - 1

#   Step 3) 상품 목록을 출력한다. [0 이상의 정수]
number = 0
while True:
    number = int(input("Intput the number of item [1 ~ ] ? = \n"))
    if number >= 0:     #   조건문 사용한 부분
        break
    print("Please enter a positive integer!!")

#   Step 4) 상품 목록을 출력한다. [상품 번호와 상품 개수를 고려하여 고객이 지불해야 할 금액을 계산하여 출력한다.]
print("------===TOTAL PRICE===------")
print(item[choice][1] * number)
