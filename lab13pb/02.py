"""
    Blackjack (EASY)

    เกมแบล็กแจ็ค (blackjack) หรือเกม 21 แต้ม เป็นเกมไพ่ที่มีการเล่นเกมแบบง่าย ๆ คือ เริ่มจากการจั่วไพ่ 2 ใบจากสำรับ ไพ่ A มีคะแนน 1 หรือ 11 คะแนน, ไพ่ 2-10 มีคะแนนตามเลขบนไพ่ และไพ่ J Q K มีคะแนน 10 คะแนน ผู้เล่นต้องการให้คะแนนรวมของไพ่บนมือมีมากที่สุด แต่ไม่เกิน 21 คะแนน เมื่อจั่วไพ่ 2 ใบแรกแล้ว ผู้เล่นสามารถเลือกที่จะหยุดหรือจั่วไพ่เพิ่มได้อีกไม่เกิน 3 ไพ่ (รวมมีไพ่บนมือไม่เกิน 5 ใบ) เพื่อให้คะแนนรวมของไพ่บนมือสูงขึ้น แต่ในขณะเดียวกันก็มีโอกาสทำให้คะแนนรวมเกิน 21 คะแนน หากคะแนนรวมของไพ่บนมือเกิน 21 คะแนน จะถือว่าผู้เล่นคนนั้นแพ้ (busted)
    เนื่องจากเกมนี้เป็นเกมที่ต้องเล่นหลายคน (multiplayer game) คุณจึงต้องการบอทที่ช่วยการฝึกซ้อม วิธีการเล่นของบอทที่ต้องการคือ บอทจะจั่วไพ่จากกองจนกว่า คะแนนรวมจะมีค่ามากกว่า 16 หรือมีไพ่บนมือครบ 5 ใบ หลังจากนั้น บอทจะแสดงคะแนนรวมที่ได้ ในกรณีที่บอทมีคะแนนรวมมากกว่า 21 คะแนน จะแสดงคำว่า “busted”
    เพื่อความง่าย จะกำหนดให้ A มีคะแนน 1 คะแนนเท่านั้น เนื่องจากคุณเป็นโปรแกรมเมอร์ คุณจึงจะเขียนบอทสำหรับฝึกซ้อมด้วยตัวเอง

    ข้อมูลเข้า
    บรรทัดแรก เป็นจำนวนกรณีทดสอบ N ชุด (1 <= N <= 100)
    ถัดมา N บรรทัด แต่ละบรรทัดจะระบุไพ่ 5 ใบที่อยู่ถัดไปในกองสำรับ ไพ่แต่ละใบสามารถเป็น A, 2, 3, …, 10, J, Q หรือ K คั่นด้วยเว้นวรรค

    ข้อมูลออก
    สำหรับแต่ละกรณีทดสอบ ให้แสดงคำตอบ 1 บรรทัด ในกรณีที่คะแนนรวมของบอทไม่เกิน 21 คะแนน ให้แสดงคะแนนรวมนั้น และในกรณีที่คะแนนรวมเกิน 21 คะแนน ให้แสดงว่า “busted” โดยไม่มีเครื่องหมายคำพูด
"""

# Draw 2 card
# Card A        =   1 (or 11)
# Card 2 - 10   =   2 - 10
# Card J Q K    =   10

# Player need most point in game but not more than 21

# Player can stop or draw more card but can't over 5 card (everycard not over 5) for make point most but this can make over 21

# Bot will draw card when point over 16 or have more thar 5 card will stop, then bot wil show current point if have over 21 will show "busted"

# psudo actions
# make drawed count var
# get first and seconds from list
# sum and check is more than 16
# if over 16 : end
# loop to draw card if less or equal 16 will get more 
# if point over end and print "busted"
# if count over end

def get_card_point(card):
    if card in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
        return int(card)
    elif card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 1

cards_list = []

test_count = int(input())
for i in range(test_count):
    x = input()
    cards_list.append(x.split(' '))

for cards in cards_list:
    count = 2
    point = get_card_point(cards[0]) + get_card_point(cards[1])

    while point <= 16 and count < 5:
        point += get_card_point(cards[count])
        count += 1

    if point > 21:
        print("busted")
    else:
        print(point)