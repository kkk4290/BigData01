# 1) 아아: 2000원 2) 라떼: 2500원
drinks = ["아이스 아메리카노", "카페라떼", "수박주스"]
prices = [2000, 2500, 4000]
amounts = [0, 0, 0]
# drinks = ["아이스 아메리카노"]
# prices = [2000]
# amounts = [0]
total_price = 0

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
    menu = input(menu_texts)
    if menu == "1":
       order_process(int(menu)-1)
    elif menu == "2":
        order_process(int(menu) - 1)
    elif menu == "3":
        order_process(int(menu) - 1)
    elif menu == "4":
        print("주문을 종료합니다")
        break
    else:
        print(f"{menu}번 메뉴는 존재하지 않습니다. 아래메누에서 골라주세요")

# print(f"{drinks[0]} {prices[0]}원 {amounts[0]}잔 {prices[0] * amounts[0]}원")
# print(f"{drinks[1]} {prices[1]}원 {amounts[1]}잔 {prices[1] * amounts[1]}원")
# print(f"{drinks[2]} {prices[2]}원 {amounts[2]}잔 {prices[2] * amounts[2]}원")
print("상품명 단가 수량 금액")
for i in range(len(drinks)):
    if amounts[i] > 0:
        print(f"{drinks[i]} {prices[i]} {amounts[i]} {prices[i] * amounts[i]}")

print(f"총 주문 금액: {total_price}원")