"""
    ลิสต์เรียงหรือไม่

    จงเขียนโปรแกรมเพื่อรับจำนวนเต็มใดๆ ที่มีค่าตั้งแต่ 0 ถึง 100 มาสร้างเป็น list โดยให้รับเข้ามาเรื่อยๆ จนผู้ใช้ใส่ -1 จึงหยุด จากนั้นให้ตรวจสอบลำดับของสมาชิกใน list และแสดงผลอย่างใดอย่างหนึ่งดังต่อไปนี้ คือ
    1) สมาชิกใน list เรียงลำดับแบบ non-increasing order นั่นคือ สมาชิกมีค่าไม่เพิ่มขึ้นจากสมาชิกในลำดับก่อนหน้า
    2) สมาชิกใน list เรียงลำดับแบบ non-decreasing order นั่นคือ สมาชิกมีค่าไม่ลดลงจากสมาชิกในลำดับก่อนหน้า
    3) สมาชิกใน list เรียงลำดับแบบสุ่ม random order นั่นคือไม่มีลำดับ
    4) สมาชิกใน list เป็นค่าเดียวกันหมด

    หมายเหตุ

    กำหนดให้มีฟังก์ชัน check_order(l) เพื่อตรวจสอบการเรียงลำดับสมาชิกใน list l และแสดงผลรูปแบบลำดับที่พบ
    ให้แสดงข้อความโต้ตอบหรือข้อผิดพลาดที่อาจเกิดขึ้นในกรณีต่างๆ ดังนี้
    “Number is out of range.”เมื่อคะแนนไม่อยู่ในช่วง 0 – 100 ซึ่งจะไม่ถูกนำมาคิดในลำดับสมาชิก
    ถ้าลิสต์ว่าง ให้พิมพ์คำว่า "The list is empty."
    ถ้าลิสต์เป็นกรณีที่ 1 ให้แสดงคำว่า "The list is in non-increasing order."
    ถ้าลิสต์เป็นกรณีที่ 2 ให้แสดงคำว่า "The list is in non-decreasing order."
    ถ้าลิสต์เป็นกรณีที่ 3 ให้แสดงคำว่า "The list is in random order."
    ถ้าลิสต์เป็นกรณีที่ 4 ให้แสดงคำว่า "The list is in non-increasing and non-decreasing order."
    คำเตือน

    list.copy() มีใน python เวอร์ชัน 3.3 ขึ้นไปเท่านั้น ใน elab ไม่มีคำสั่งนี้ ให้นิสิตก็อปปี้ลิสต์เอง
"""

def check_order(l):
    if len(l) == 0:
        return 'The list is empty.'
    
    is_non_increase = False
    is_non_decrease = False

    temp_value = None

    for value in l:
        if temp_value == None:
            temp_value = value
        elif value > temp_value:
            temp_value = value
            is_non_increase = True
        elif value < temp_value:
            temp_value = value
            is_non_decrease = True

    if not is_non_increase and not is_non_decrease:
        return 'The list is in non-increasing and non-decreasing order.'
    elif is_non_increase and is_non_decrease:
        return 'The list is in random order.'
    elif is_non_increase:
        return 'The list is in non-decreasing order.'
    elif is_non_decrease:
        return 'The list is in non-increasing order.'

ls = []

while True:
    x = int(input('Enter a number (-1 to end): '))

    if x == -1:
        break

    if x < 0 or x > 100:
        print('Number is out of range.')
        continue

    ls.append(x)

print('-----')
print('Original list:')
print(ls)
print(check_order(ls))