provinces = {
    'central': ['Bangkok', 'Samut Prakan', 'Nonthaburi', 'Samut Sakhon', 'Ayutthaya', 'Pathum Thani'],
    'northern': ['Chiang Mai', 'Chiang Rai', 'Lamphun', 'Lampang', 'Mae Hong Son', 'Nan'],
    'northeastern': ['Roi Et', 'Chaiyaphum', 'Loei', 'Nong Khai', 'Sakon Nakhon', 'Surin'],
    'southern': ['Surat Thani', 'Krabi', 'Phuket', 'Yala', 'Songkhla', 'Narathiwat']
}

# while True:
#     x = input()

#     if x == '':
#         break

#     [province, region] = x.split(':')

#     if region in provinces and province in provinces[region]:
#         print('Yes')
#     else:
#         print('No')

for region in provinces:
    for province in provinces[region]:
        print(f'{province}:{region}')