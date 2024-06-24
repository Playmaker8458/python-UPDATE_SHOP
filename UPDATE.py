# function csai_shop_process เก็บรายการที่ขายในรูปแบบ dictionary

def csai_shop_process():
    # ราคาสินค้า
    dict_csai_shop = {"price_product" : 
        {"notebook" : 34000, "taplate" : 19000, "Mobile phone" : 26000}
    }
    # คืนค่า dict_csai_shop โดยการเข้าถึงคีย์หลัก เพื่อทำการส่งค่า key และ value กลับไปเพื่อให้ด้านนอก function ทำการเก็บผลลัพธ์เป็น dictionary ให้ {"notebook" : 34000, "taplate" : 19000, "Mobile phone" : 26000}
    return dict_csai_shop["price_product"] 

def amount_input(prompt : str) -> int:
    while True:
        try:
            product_input = int(input(prompt))
            if product_input > -1:
                return product_input
            else:
                print("กรุณากรอกเข้ามาทำงานใหม่อีกครั้ง: ")
        except (ValueError, KeyboardInterrupt):
            print("error".upper())

def amount_product(amount_notebook : int, amount_taplate : int, amount_Mobile : int) -> list:
    List_amount = [amount_notebook, amount_taplate, amount_Mobile]
    return List_amount

def calculate_pricess(*prefix) -> tuple:
    original_price = ( 
        (prefix[0] * prefix[1]), 
        (prefix[2] * prefix[3]), 
        (prefix[4] * prefix[5]), 
    )
    return original_price

def discount_price_process(sum_price : int) -> int:
    if sum_price > 50000:
        return 10
    else:
        return 0

def input_member(prompt : str) -> str:
    while True:
        try:
            member = input(prompt).upper()
            return member
        except KeyboardInterrupt:
            print("error".upper())
    
def discount_member_process(member : str) -> int:
    if member == "Y":
        return 5
    else:
        return 0

# def input_money(prompt : str) -> int:
#     while True:
#         try:
#             money = int(input(prompt))
#             return money
#         except (ValueError, KeyboardInterrupt):
#             print("error".upper())

def Receipt_input(*prefix):
    while True:
        try:
            money = int(input(prefix[0]))
            if money < prefix[1]:
                print("กรุณากรอกจำนวนเงินเข้ามาทำงานใหม่อีกครั้ง")
            else:
                amount_price = money - prefix[1]
                print("🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸 ใบเสร็จ 🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸")
                if prefix[4] > 0:
                    print(f"1.Notebook {prefix[4]} เครื่อง ราคา {prefix[7]:,.2f} บาท")
                if prefix[5] > 0:
                    print(f"2.Tablet {prefix[5]} เครื่อง ราคา {prefix[8]:,.2f} บาท")
                if prefix[6] > 0:
                    print(f"3.Mobile cs Phone {prefix[6]} เครื่อง ราคา {prefix[9]:,.2f} บาท")
                print(f"\nรายการทั้งหมด {prefix[4] + prefix[5] + prefix[6]} รายการ")
                print(f"ราคารวมก่อนหักส่วนลด: {prefix[2]:,.2f} บาท")
                print(f"ยอดส่วนลด: {prefix[3]:,.2f} บาท")
                print(f"จำนวนเงินทอน: {amount_price:,.2f} บาท")
                print("🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸🌸")
                break
        except (ValueError, KeyboardInterrupt):
            print("error".upper())