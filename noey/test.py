#this pb is difficult bc of tax
#pass บอกไม่ให้errorเวลายังไม่มีcode
#ิbreak ใช้ในloop

age = int(input('Enter your age: '))
income = int(input('Enter your net income: '))
nit = 0
x = income - 30000

''' incorrect
#              True                             True
#   True  or   False                  True  or    True     
if income > 1 or income <= 30000 and (age >= 15 or age <= 60): 
#orผิด เช่น-500 : -500 > 1 false , -500 < 30000 true มันผิดกรณีหลัง ต้องใช้and
    nit = (income*20)/100
    print(f'Your negative income tax is {nit:.2f} Baht.')
elif income > 30000 or income <= 79999 and (age >= 15 or age <= 60):
    nit = (x*12)/100
    print(f'Your negative income tax is {nit:.2f} Baht.')
elif income > 80000 and (age >= 15 or age <= 60):
    nit = (income*0)/100
    print(f'Your negative income tax is {nit:.2f} Baht.')
else: #เขาให้ปริ้นอันเดียว
    print("Invalid income.")
    print("Invalid age.")
'''


age = 79

#          true
#     false        true
if age < 15 or age > 60:
    print('Invalid age.')
elif income < 1 or income > 79999:
    print('Invalid income.')
elif income >= 1 and income <= 30000:
    nit = (income * 20) / 100
    print(f'Your negative income tax is {nit:.2f} Baht.')

#setใหญ่ แล้วก็มีsubsetย่อย
if (age >= 15 and age <= 60) and (income >= 1 and income <= 79999):
    if income > 1 and income <= 30000:
        nit = (income*20)/100
        print(f'Your negative income tax is {nit:.2f} Baht.')
    elif income > 30000 and income <= 79999:
        nit = (x*12)/100
        print(f'Your negative income tax is {nit:.2f} Baht.')
    elif income > 80000:
        nit = (income*0)/100
        print(f'Your negative income tax is {nit:.2f} Baht.')
elif age < 15 and age >60:
        print("Invalid age.")
elif income < 1:
        print("Invalid income.")
        
    
    

# ตัวใดตัวหนึ่งเป็น True (or)
# False or True or False

#จริงทั้งหมด (and)