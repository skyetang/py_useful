# coding:utf-8

work = {}
one_value = (1,)
one_key = 1
work[str(one_key)] = one_value
print(work)

two_key = 2
two_value = []
two_value.append(1)
two_value.append(2)
work[str(two_key)] = two_value

three_key = 3
three_value = []
three_value.append(1)
three_value.append(2)
three_value.append(3)
work[str(three_key)] = three_value
print(work)

four_key = 4
four_value = []
four_value.append(1)
four_value.append(2)
four_value.append(3)
four_value.append(4)
work[str(four_key)] = four_value

temp_five = (1, 2, 3, 4, 5)
five_key = 5
five_value = []
five_value.extend(temp_five)
work[str(five_key)] = five_value
print(work)

temp_six = (1, 2, 3, 4, 5, 6)
six_key = 6
six_value = []
six_value.extend(temp_six)
work[str(six_key)] = six_value

temp_seven = {1, 2, 3, 4, 5, 6, 7}
seven_key = 7
seven_value = []
seven_value.extend(temp_seven)
work[str(seven_key)] = seven_value

temp_eight = [1, 2, 3, 4, 5, 6, 7, 8]
eight_key = 8
eight_value = []
eight_value.extend(temp_eight)
eight_key = str(eight_key)
work[eight_key] = eight_value
print(work)

temp_nine = (1, 2, 3, 4, 5, 6, 7, 8, 9)
nine_key = 9
nine_value = list(temp_nine)
nine_key = str(nine_key)
work.update({nine_key:nine_value})
print(work, type(work))

_keys = work.keys()
keys = list(_keys)
print(keys)





one = keys[0]
one_value = work.pop(one)
print('{}*{}={}'.format(one, one_value[0], int(one) * one_value[0]))

two = keys[1]
two_value = work.pop(two)
print('{}*{}={}'.format(two, two_value[0], int(two) * two_value[0]), end=' ')
print('{}*{}={}'.format(two, two_value[1], int(two) * two_value[1]))