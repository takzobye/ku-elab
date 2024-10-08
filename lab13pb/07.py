"""
    Minesweeper

    เขียนโปรแกรมเพื่อระบุจำนวนทุ่นระเบิด ที่อยู่รอบแต่ละช่อง ในตารางขนาด m x n ใด ๆ
    โดยช่องที่เป็นทุ่นระเบิดให้แทนด้วย *
    ช่องที่ไม่ใช่ทุ่นระเบิด ให้แสดงจำนวนทุ่นระเบิดที่อยู่รอบช่องนั้นว่ามีกี่ลูก (8 ทิศรอบช่องนั้น)

    ข้อมูลเข้า
    บรรทัดแรก รับจำนวนเต็มบวก m และ n คั่นด้วย x ซึ่งเป็นขนาดของตาราง m x n
    บรรทัดที่สอง รับจำนวนเต็มบวก p แทนจำนวนของทุ่นระเบิดทั้งหมดที่อยู่ในตาราง
    p บรรทัดต่อมา แต่ละบรรทัด รับจำนวนเต็ม x และ y คั่นด้วย , แทนพิกัด x, y ของทุ่นระเบิดในตาราง โดยมุมซ้ายบนสุดคือพิกัด (0, 0)
    ข้อมูลนำเข้าจะเป็นข้อมูลที่ถูกต้องเสมอ (เช่น พิกัด (x, y) ของทุ่นระเบิด จะอยู่ในตารางขนาด m x n เสมอ)

    ข้อมูลออก
    m บรรทัด แต่ละบรรทัด แสดง n ตัวอักษร แทน n ช่อง แต่ละช่องประกอบด้วย ทุ่นระเบิดซึ่งแทนด้วย * หรือจำนวนทุ่นระเบิดรอบช่องนั้นซึ่งแทนด้วย ตัวเลข 0-8
"""

width, height = [ int(x) for x in input().split('x') ]
bomb_count = int(input())

bomb_locations = []

for i in range(bomb_count):
    xy = [ int(x) for x in input().split(',') ]
    bomb_locations.append(xy)

for x in range(width):
    line = ''

    for y in range(height):
        if [x, y] in bomb_locations:
            line += '*'
        else:
            count = 0

            if [x - 1, y + 1] in bomb_locations:
                count += 1

            if [x, y + 1] in bomb_locations:
                count += 1

            if [x + 1, y + 1] in bomb_locations:
                count += 1

            if [x + 1, y] in bomb_locations:
                count += 1

            if [x + 1, y - 1] in bomb_locations:
                count += 1

            if [x, y - 1] in bomb_locations:
                count += 1

            if [x - 1, y - 1] in bomb_locations:
                count += 1

            if [x - 1, y] in bomb_locations:
                count += 1

            line += str(count)

    print(line)