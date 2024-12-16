"""
    จงเขียนฟังก์ชัน namelist(names) ที่รับ parameter names ซึ่งเป็น list ของชื่อคนซึ่งเป็น string
    โดยฟังก์ชัน namelist(names) นี้ จะต้องคืนค่า string ที่เป็นข้อความที่เชื่อมทุกชื่อคนใน list ด้วย , ยกเว้นคู่สุดท้าย ให้เชื่อมด้วย & (ไม่มีช่องว่างหน้าเครื่องหมาย , แต่มีช่องว่างหลังเครื่องหมาย , หน้าเครื่องหมาย & และหลังเครื่องหมาย &)
"""

def namelist(names):
    if len(names) == 0:
        return ''
    
    if len(names) == 1:
        return names[0]
    
    if len(names) == 2:
        return f'{names[0]} & {names[1]}'
    
    text = ''
    count = 0

    for name in names:
        if count == 0:
            text += name
        elif count + 1 != len(names):
            text += f', {name}'
        else:
            text += f' & {name}'

        count += 1 

    return text

print( namelist(['Bart', 'Viola', 'Peter', 'Nostel']) )
print( namelist(['Bart', 'Viola']) )
print( namelist(['Peter']) )
print( namelist([]) == '' )

