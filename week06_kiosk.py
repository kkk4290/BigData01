# 1) 아아: 2000원 2) 라떼: 2500원
drinks = ["아이스 아메리카노", "카페 라떼", "수박 주스", "딸기 주스"]
prices = [2000, 2500, 4000, 4200]
# drinks = ["아이스 아메리카노"]
# prices = [2000]
total_price = 0
#amounts = [0 for _ in range(len(drinks))] #list comprehension(리스트 축약)
amounts = [0] * len(drinks)

def order_process(index):
    """
    주문 처리 함수 1) 주문 디스플레이 2) 총 주문 금액 누산 3) 주문 품목 수량 업데이트
    :return: 없음
    """
    global  total_price
    print(f"{drinks[index]}를 주문하셨습니다. 가격은 {prices[index]}원 입니다")
    total_price = total_price + prices[index]
    amounts[index] = amounts[index] + 1

menu_texts = ""
for j in range(len(drinks)):
    menu_texts = menu_texts + f"{j+1}) {drinks[j]} {prices[j]}원 "
menu_texts = menu_texts + f"{len(drinks)+1}) 주문종료:"

while True:
    menu = int(input(menu_texts))
    if len(drinks) >= menu >= 1:
        order_process(menu - 1)

    elif menu == len(drinks) + 1:
        print("주문을 종료합니다")
        break
    else:
        print(f"{menu}번 메뉴는 존재하지 않습니다. 아래메누에서 골라주세요")


print("상품명 단가 수량 금액")
for i in range(len(drinks)):
    if amounts[i] > 0:
        print(f"{drinks[i]} {prices[i]} {amounts[i]} {prices[i] * amounts[i]}")

print(f"총 주문 금액: {total_price}원")