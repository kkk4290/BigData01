#open api : wttr.in (weather info)
import kiosk as kk
import requests

if __name__ == "__main__":
    #url = f"http://wttr.in/suwon?format=%C+%t&lang=ko"
    #url = f"http://naver.com/kim"  #404 page not found
    url = f"http://wttr123.in/suwon?format=%C+%t&lang=ko"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(response.text.strip())
        else:
            print(f"상태코드: {response.status_code}")
    except Exception as err:
        print(f"오류: {err}")
    kk.run()
    kk.print_receipt()
    kk.get_ticket_number()
