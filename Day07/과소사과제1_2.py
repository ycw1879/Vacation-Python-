print("☆★좌석 예매 프로그램☆★")
seat=[0,0,0,0,0,0,0,0,0,0]  # 좌석 번호 초기화   
while True:
    print("좌석을 예약하시겠습니까?(YES or NO)")
    movie=input("")
    if movie=="YES" or movie=="yes":
        print("원하는 좌석을 선택하세요 :")
        pick=int(input("1번~10번")) # 좌석번호 입력
        if pick>=1 and pick<=10: # 입력한 좌석번호가 1~10사이일때만 조건식 실행
            if (seat[pick-1])==0: # seat리스트의 좌석번호값이 0과 같다면 
                seat[pick-1]=1 # 좌석번호값을 1로 변경
                print(pick,"번 좌석이 예매되었습니다.!!!")
                print("--------------------------------------")
                print(seat)     #seat리스트 출력
                print("--------------------------------------")
        
            else:
                print("이미 예약된 자리입니다.")
    elif movie=="NO" or movie=="no":
        print("좌석예매를 종료합니다.")
        break # 반복문 종료
    else:
        continue # 다음 조건으로 이동 
