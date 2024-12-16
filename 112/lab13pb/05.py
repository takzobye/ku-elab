"""
ผลบวกของเลข Fibonacci

เลข Fibonacci F(n) มีนิยามดังนี้

F(0) = 1

F(1) = 1

F(2) = F(0) + F(1) = 2

F(3) = F(1) + F(2) = 3

.

.

F(n) = F(n-2) + F(n-1)

ดังนั้นลำดับ Fibonacci เมื่อ n เป็น 6 จึงมีค่าดังนี้ 1, 1, 2, 3, 5, 8, 13

ให้นิสิตเขียนโปรแกรมรับค่า n และตัวอักษร 1 ตัว จากนั้นให้สร้างลำดับ Fibonacci ตั้งแต่ F(0) ถึง F(n) และคำนวณผลรวมของลำดับ Fibonacci ตามตัวอักษรนั้น นั่นคือ

ถ้าตัวอักษรเป็น "e" หรือ "E" ให้แสดงผลบวกของ F(i) เมื่อ 0 <= i <= n และ i เป็นเลขคู่
ถ้าตัวอักษรเป็น "o" หรือ "O" ให้แสดงผลบวกของ F(i) เมื่อ 0 <= i <= n และ i เป็นเลขคี่
เช่น เมื่อ n=6 และตัวอักษรเป็น e เราจะแสดงค่าของ F(0)+F(2)+F(4)+F(6) = 1+2+5+13 =21

ถ้าข้อมูลเข้าผิดพลาดให้พิมพ์คำว่า "ERROR" แล้วจบการทำงาน
"""

def fibo(n):
    if n == 0 or n == 1:
        return 1

    return fibo(n - 2) + fibo(n - 1)

n = int(input())
sign = input()

start_num = -1

if n < 0:
    print("ERROR")
elif n == 0 and (sign == 'o' or sign == 'O'):
    print("ERROR")
elif sign == 'e' or sign == 'E':
    start_num = 0
elif sign == 'o' or sign == 'O':
    start_num = 1
else:
    print("ERROR")
    
if start_num == 0 or start_num == 1:
    if n == 0:
        print(1)
    else:
        sum = 0
        for i in range(start_num, n + 1, 2):
            sum += fibo(i)

        print(sum)