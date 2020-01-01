#   날짜 : 1월 1일
#   작성자 : 윤찬우
#   프로그램 : 과제1_02(while, if, break, continue 사용)

seat = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while True:
    #   Step 1) 좌석을 예약하시겠습니까?를 출력 후 YES 또는 NO를 입력 받는다.
    reservation = input("좌석을 예약하시겠습니까? [YES or NO]\n")
    #   Step 1_1) YES를 입력하면 원하는 좌석을 선택할 수 있다.(좌석은 1 ~ 10번 중 정수 선택)
    if reservation == "YES":
        while True:
            select_seat = int(input("원하는 좌석을 선택하세요 : \n1번 ~ 10번"))
            if select_seat < 1 and select_seatq > 10:
                continue
            #   Step 1_2) 예약이 완료되면 해당 좌석이 0에서 1로 바뀐다.
            if seat[select_seat - 1] == 0:
                seat[select_seat - 1] = 1
                print(str(select_seat)+"번 좌석이 예매되었습니다.!!!!")
                print("------------------------------")
                print(seat)
                print("------------------------------")
                break
            #   Step 1_3) 이미 예약된 좌석은 이미 예약된 자리입니다.를 출력한다.
            else:
                print("이미 예약된 자리입니다.")
                break
    #   Step 2_1) NO를 입력하면 프로그램을 종료한다.
    elif reservation == "NO":
        print("좌석예매를 종료합니다.")
        break
    #   Step 3_1) YES 또는 NO가 아닌 다른 문자열을 입력하면 좌석을 예약하시겠습니까?로 되돌아 간다.
    else:
        continue
