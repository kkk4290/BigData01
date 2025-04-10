# 1) 아아: 2000원 2) 라떼: 2500원
drinks = ["아이스 아메리카노", "카페라떼"]
prices = [2000, 2500]
while True:
    menu = input(f"1) {drinks[0]} {prices[0]}2) {drinks[1]}{prices[1]}3) 주문종료:")
    if menu == "1":
        print(f"아이스 아메리카노를 주문하셨습니다. 가격은 {prices[0]}원 입니다")
    if menu == "2":
        print(f"카페라떼를 주문하셨습니다. 가격은 {prices[1]}원 입니다")
    if menu == "1":
        print("주문을 종료합니다")
        break