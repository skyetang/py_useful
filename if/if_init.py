# coding:utf-8

info = 'my name is aiya'

info_list = info.split()
print(info_list)

if info_list[0] == 'aiya':
    print(0)
    info_list[0] = 'yige'

if info_list[1] == 'aiya':
    print(1)
    info_list[1] = 'yige'

if info_list[2] == 'aiya':
    print(2)
    info_list[2] = 'yige'

if info_list[-1] == 'aiya':
    print(-1)
    info_list[-1] = 'yige'

print(info_list)
info = ' '.join(info_list)
print(info)

info = 'my name is aiya, i am a pythoner, i love python'
info_list = info.split()

if info_list[0] in ['python', 'i']:
    info_list[0] = '*'

if info_list[1] == 'python' or info_list[1] == 'i':
    info_list[1] = '*'

if info_list[2] == 'python' or info_list[2] == 'i':
    info_list[2] = '*'

if info_list[3] == 'python' or info_list[3] == 'i':
    info_list[3] = '*'

if info_list[4] == 'python' or info_list[4] == 'i':
    info_list[4] = '*'

if info_list[5] == 'python' or info_list[5] == 'i':
    info_list[5] = '*'

if info_list[6] == 'python' or info_list[6] == 'i':
    info_list[6] = '*'

if info_list[7] == 'python' or info_list[7] == 'i':
    info_list[7] = '*'

if info_list[8] == 'python' or info_list[8] == 'i':
    info_list[8] = '*'

if info_list[9] == 'python' or info_list[9] == 'i':
    info_list[9] = '*'

if info_list[-1] in ['python', 'i']:
    info_list[-1] = '*'

print(info_list)
info = ' '.join(info_list)
print(info)

info = 'my name is aiya'
print(len(info))
if len(info) > 14 and len(info) != 17:
    print(info.replace('aiya', 'yige'))



