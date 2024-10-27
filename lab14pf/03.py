"""first way not use math"""
# x = input()
# num = int(input())
# majors = x.split(',')
# majors += (majors[1:] * num)
# print(majors[num - 1])

"""second way use math"""
x = input()
num = int(input())
majors = x.split(',')
target = (num - 1) % 7
print(majors[:len(majors)][target])