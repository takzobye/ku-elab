"""
    จำนวนวันอาทิตย์

    ให้เขียนโปรแกรมรับวันที่สองวัน โดยรูปแบบคือ วัน-เดือน ที่มีเครื่องหมาย "-" คั่นกลาง และวันกับเดือนเป็นเลขจำนวนเต็มสองหลักที่อาจมี 0 นำหน้า เช่นวันที่ 11 ธันวาคมจะเขียนเป็น "11-12" หรือวันที่ 3 สิงหาคมจะเขียนเป็น "03-08"
    จากนั้นให้รับวันที่เป็นวันอาทิตย์แรกของเดือนมกราคม จากนั้นพิมพ์จำนวนวันอาทิตย์ที่อยู่ในช่วงของวันที่สองวันข้างต้น กำหนดให้เดือนกุมภาพันธ์มี 28 วัน

    ข้อมูลที่ผิดพลาด
    - ถ้าเดือนที่รับเข้ามาผิดให้พิมพ์คำว่า "Wrong Month"
    - ถ้าวันที่ที่รับเข้ามาผิดหรือวันอาทิตย์แรกของเดือนมกราคมผิดให้พิมพ์คำว่า "Wrong Day"
    - ถ้าทั้งวันที่และเดือนผิดให้พิมพ์ "Wrong Month" ก่อน "Wrong Day" คนละบรรทัดกัน
    - พิมพ์ "Wrong Month" ครั้งเดียวแม้ว่าเดือนจะผิดทั้งสองวันที่ และพิมพ์ "Wrong Day" แค่ครั้งเดียวถึงแม้วันจะมากกว่าหนึ่งแห่งที่ผิด
"""

# receive 2 date
# get start date in jan

# make fxcking psuedo code in this problem
# make list for date count in each month
# get first date
# get second date
# get start date in jan
# compare start and end date between first date and second date
# make count var
# start loop while
# break if over end date
# plus count if more that start date
# ...

def is_valid_month(month):
    return month > 12

def is_valid_day(day, month):
    if month > 12:
        return True

    if day > DAY_COUNT_LIST[month - 1]:
        return False

    return True

def sort_date(first_date, second_date):
    # compare month
    if first_date[1] > second_date[1]:
        return [second_date, first_date]
    elif second_date[1] > first_date[1]:
        return [first_date, second_date]
    
    # compare day (if come this compare that mean month is equal)
    if first_date[0] > second_date[0]:
        return [second_date, first_date]
    elif second_date[0] > first_date[0]:
        return [first_date, second_date]

    return [first_date, second_date]

def is_over_date(current_date, end_date):
    if current_date[1] > end_date[1]:
        return True
    elif current_date[1] == end_date[1]:
        if current_date[0] > end_date[0]:
            return True
    return False

def is_in_range_date(current_date, start_date, end_date):
    if start_date[1] < current_date[1] < end_date[1]:
        return True
    elif start_date[1] == current_date[1]:
        if start_date[0] <= current_date[0]:
            return True
    elif current_date[1] == end_date[1]:
        if current_date[0] <= end_date[0]:
            return True
        
    return False

def get_sunday_count(first_date, second_date, first_sunday):
    is_break = False

    if is_valid_month(first_date[1]) or is_valid_month(second_date[1]):
        is_break = True
        print('Wrong Month')

    if not is_valid_day(first_date[0], first_date[1]) or not is_valid_day(second_date[0], second_date[1]) or (first_sunday < 1 or first_sunday > 31):
        is_break = True
        print('Wrong Day') 

    if is_break: 
        return
    
    start_date, end_date = sort_date(first_date, second_date)

    count = 0
    current_date = [first_sunday, 1]

    while True:
        current_day = current_date[0]
        current_month = current_date[1]
        day_count = DAY_COUNT_LIST[current_month - 1]

        if is_over_date(current_date, end_date):
            break

        if is_in_range_date(current_date, start_date, end_date):
            count += 1

        if current_day + 7 <= day_count:
            current_date = [current_day + 7, current_month]
        else:
            remain_day = day_count - current_day
            current_date = [7 - remain_day, current_month + 1]
    
    print(count)

DAY_COUNT_LIST = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

date1 = [ int(datemonth) for datemonth in input().split('-') ]
date2 = [ int(datemonth) for datemonth in input().split('-') ]
sunday = int(input())

get_sunday_count(date1, date2, sunday)