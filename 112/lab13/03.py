"""
    Ex.1 จงเขียน function definition ของฟังก์ชัน filter_sort_factors_3_7(ls) ที่รับ parameter เป็น List ของจำนวนเต็ม ls
    ฟังก์ชันนี้จะคืนค่า List ที่มีข้อมูล 2 ค่า
    ค่าแรกคือ List ของจำนวนเต็มบวกใน List ls ที่มี 3 หรือ 7 เป็นตัวประกอบ โดยเรียงค่าข้อมูลจากน้อยไปมาก
    ค่าที่สองคือ List ของจำนวนเต็มบวกใน List ls ที่ไม่มี 3 และ ไม่มี 7 เป็นตัวประกอบ โดยเรียงค่าข้อมูลจากมากไปน้อย
"""

def filter_sort_factors_3_7(ls):
    factors_ls = []
    not_factors_ls = []

    for v in ls:
        if v > 0:
            if v % 3 == 0 or v % 7 == 0:
                factors_ls.append(int(v))
            else:
                not_factors_ls.append(v)

    factors_ls.sort()
    not_factors_ls.sort(reverse=True)

    return [factors_ls, not_factors_ls]