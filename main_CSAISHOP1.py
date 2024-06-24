import os
import time
from processes7 import *

print("============== Welcome to csai-shop ==============")
print("""\
1.notebook        34,000 baht.
2.Tablet          45,000 baht.
3.Mobile cs Phone 46,000 baht.""")
print("==================================================")
price_all = csai_shop_process() # ตัวแปร price_all ทำการเก็บค่า dictionary ที่เข้าถึงคีย์หลัก จากฟังก์ชั่น csai_shop_process เพื่อคืนค่าและราคาในรูปแบบ dict   
price_notebook, price_taplate, price_Mobile = price_all["notebook"], price_all["taplate"], price_all["Mobile phone"]

amount_notebook = amount_input("Enter you amount notebook: ")
amount_taplate = amount_input("Enter you amount taplate: ")
amount_Mobile = amount_input("Enter you amount Mobile: ")
notebook_amount, taplate_amount, Mobile_amount = amount_product(amount_notebook, amount_taplate, amount_Mobile)
os.system('cls'); time.sleep(1.5)

summation_price = sum(calculate_pricess(amount_notebook, price_notebook, amount_taplate, price_taplate, amount_Mobile, price_Mobile))
print("="*50+f"\nราคารวมทั้งหมด : {summation_price:,.2f} บาท\n"+"="*50)
discount_price = discount_price_process(sum_price=summation_price)
notebook_price, tablet_price, Mobile_price = calculate_pricess(amount_notebook, price_notebook, amount_taplate, price_taplate, amount_Mobile, price_Mobile)

member_input = input_member("Enter you member (Y : YES, N : NO): ")
discount_member = discount_member_process(member=member_input)
os.system('cls'); time.sleep(1.5)

summation_discount = discount_price + discount_member
discount = summation_price * (summation_discount / 100)
Reduced_price =  summation_price - discount 
print("="*50+f"\nราคาสินค้าที่ลดแล้ว : {Reduced_price:,.2f} บาท\n"+"="*50)

money_input = input_money("Enter you money: ")
os.system('cls'); time.sleep(1.5)
Receipt_input(money_input, Reduced_price, summation_price, discount, notebook_amount, taplate_amount, Mobile_amount, notebook_price, tablet_price, Mobile_price)