# coding:utf-8

def cap(data):
    index = 0
    temp = ''
    for item in data:
        if index == 0:
            temp = item.upper()
        else:
            temp += item
        index += 1
    print('for结束了')
    return temp
    print('finished')


result = cap('hello aiya')
print(result)


def message(message, message_type):
    new_message = '[%s] %s' % (message_type, message)
    print(new_message)


print(message('天气真好', 'info'))


def test():
    for i in range(10):
        print(i)
        if i == 5:
            return i


print(test())