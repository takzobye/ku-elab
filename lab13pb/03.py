"""
    ให้นิสิตเขียนโปรแกรมทอนเงิน แต่ครั้งนี้ให้จำนวนและมูลค่าของธนบัตรนั้นถูกกำหนดโดยผู้ใช้

    โปรแกรมจะรับข้อมูลจำนวนของประเภทธนบัตร (n) มาก่อนในบรรทัดแรก จากนั้นบรรทัดที่ 2 ถึง n+1 จะรับมูลค่าของธนบัตรทีละใบ มูลค่าของธนบัตรที่ใส่เข้ามาอาจไม่เรียงลำดับก็ได้ จากนั้นโปรแกรมจะรับจำนวนเงินที่จะต้องทอนในบรรทัดสุดท้าย

    โปรแกรมจะพิมพ์จำนวนธนบัตรแต่ละประเภทที่ต้องทอน โดยพิมพ์เรียงลำดับมูลค่าธนบัตรจากมากไปน้อย โดยการทอนเงินจะใช้หลักการว่าจะใช้ธนบัตรที่มีมูลค่ามากที่สุดเท่าที่จะทำได้ และจำนวนธนบัตรมีไม่จำกัด
"""

# loop each money type

# check if current_amount += each money not over target_emount
# current_amount += each money
# if over change each and print

money_types = []
money_type_count = int(input())

for i in range(money_type_count):
    x = int(input())
    money_types.append(x)

money_types.sort(reverse=True)

target_amount = int(input())
current_amount = 0

for money_type in money_types:
    count = 0 

    while current_amount + money_type <= target_amount:
        current_amount += money_type
        count += 1

    print(f'{money_type}: {count}')