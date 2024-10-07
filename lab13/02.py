"""
    Ex.1 จงเขียน function definition ของฟังก์ชัน count_factors_3_7(ls) ที่รับ parameter เป็น List ของจำนวนเต็ม ls
    ฟังก์ชันนี้จะคืนค่า จำนวนของจำนวนเต็มบวกใน List ls ที่มี 3 หรือ 7 เป็นตัวประกอบว่ามีทั้งหมดกี่ตัว
"""

def count_factors_3_7(ls):
    count = 0
    for v in ls:
        if v % 3 == 0 or v % 7 == 0:
            count += 1

    return count

"""
    Ex.2 จงเขียน function definition ของฟังก์ชัน filter_factors_3_7(ls) ที่รับ parameter เป็น List ของจำนวนเต็ม ls
    ฟังก์ชันนี้จะคืนค่า List ที่มีข้อมูล 2 ค่า
    ค่าแรกคือ List ของจำนวนเต็มบวกใน List ls ที่มี 3 หรือ 7 เป็นตัวประกอบ
    ค่าที่สองคือ List ของจำนวนเต็มบวกใน List ls ที่ไม่มี 3 และ ไม่มี 7 เป็นตัวประกอบ
"""

def filter_factors_3_7(ls):
    factors_ls = []
    not_factors_ls = []

    for v in ls:
        if v > 0:
            if v % 3 == 0 or v % 7 == 0:
                factors_ls.append(int(v))
            else:
                not_factors_ls.append(v)

    return [factors_ls, not_factors_ls]