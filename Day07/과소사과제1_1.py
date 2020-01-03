# 상품 판매 가격
price1 = 5000
price2 = 2000
price3 = 3000
# 상품 목록 : 출력 및 입력
print("*** Item ***")
print("1. Cabbage")
print("2. Daikon")
print("3. Lettuce")
print("Select Item (1~3) ? =")
goodsIdx = int(input())

print("Input the number of item (1~) ? =")
goodsNum = int(input(""))


# 조건문
priceTotal = 0
if goodsIdx == 1 :
    priceTotal = price1*goodsNum
elif goodsIdx == 2 :
    priceTotal = price2*goodsNum

elif goodsIdx == 3 :
    priceTotal = price3*goodsNum
# 결과 출력
print("*** Total Price ***")
print(priceTotal)

