"""
ลูกของสิงโตและเสือเรียกว่า liger (Mix Name)
    นำชื่อพ่อพันธุ์ส่วนที่อยู่ก่อนสระตัวที่สอง มาผสมกับชื่อของแม่พันธุ์ส่วนที่อยู่หลังสระตัวแรก
"""

"""
dad = ก่อนสระตัวที่สอง
mom = หลังสระตัวแรก
"""

"""
How 
1. get index from dad
2. get index from mom
3. slice both
"""

dad = input()
mom = input()

dad_index = -1
dad_count = 0

for i in range(len(dad)):
    char = dad[i]

    if char in 'aeiou':
        dad_count += 1

        if dad_count == 2:
            dad_index = i
            break

if dad_index != -1:
    dad = dad[:dad_index]

mom_index = -1
mom_count = 0

for i in range(len(mom)):
    char = mom[i]

    if char in 'aeiou':
        mom_index = i + 1
        break

if mom_index != -1:
    mom = mom[mom_index:]

print(dad + mom)

"""
dad = ก่อนสระตัวที่สอง
mom = หลังสระตัวแรก

ant
butterfly

result : anttterfly
"""