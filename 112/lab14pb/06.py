# input get exams count
# input get 2 data (checkin, exam_pass)
# input int nisit count

# while input get checkin
# while input get score

# print can't sob
# print nitist num, percent checkin, percent exam pass () = mean can't sob

exams = input().split()
exam_count = 0

for score in exams:
    exam_count += int(score)

check_in_criterion, exam_pass_criterion = input().split()
check_in_criterion = float(check_in_criterion)
exam_pass_criterion = float(exam_pass_criterion)

nisit_count = int(input())

nisit_data = []

for i in range(nisit_count):
    x = input().split()
    checked_count = x.count('1')
    not_checked_count = x.count('0')

    nisit_data.append({
        'checkin': checked_count / (checked_count + not_checked_count) * 100,
        'exam': 0
    })

for i in range(nisit_count):
    x = [ int(score) for score in input().split() ]
    nisit_data[i]['exam'] = sum(x) / exam_count * 100

nisit_cant_sob = 0
for i in range(nisit_count):
    nisit = nisit_data[i]
    if nisit['checkin'] < check_in_criterion and nisit['exam'] < exam_pass_criterion:
        nisit_cant_sob += 1

print(nisit_cant_sob)

for i in range(nisit_count):
    nisit = nisit_data[i]

    if nisit['checkin'] < check_in_criterion and nisit['exam'] < exam_pass_criterion:
        print(f'({i + 1}) {nisit['checkin']:.2f} {nisit['exam']:.2f}')
    else:
        print(f'{i + 1} {nisit['checkin']:.2f} {nisit['exam']:.2f}')