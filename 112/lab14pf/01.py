"""
Bigrams (simple)
    Bigrams คือ ตัวอักษรสองตัวติดกันทั้งหมด ที่ได้จากคำ หรือประโยค เช่น คำว่า Hello จะมี bigrams เป็น 'He', 'el', 'll', และ 'lo' 
    ให้เขียนโปรแกรม python รับอินพุตเป็นคำภาษาอังกฤษ 1 คำ แล้วแสดง bigrams ของคำดังกล่าว ในรูปแบบเป็นตัวอักษรโรมันตัวพิมพ์เล็กทั้งหมด 
    เรียงลำดับแบบ ascending (น้อยไปมาก) บรรทัดละหนึ่ง bigram และไม่แสดง bigram ที่ซ้ำกัน
"""

# Hello
# computerscience

text = input()

ls = []
st = ''

for char in text:
    st += char.lower()

    if len(st) == 2:
        if st not in ls:
            ls.append(st)
        
        st = st[1:]

ls.sort()

for v in ls:
    print(v)