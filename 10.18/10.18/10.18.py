#coding:utf-8

# 基本数据类型
counter = 100
miles = 1000.0
name = 'runoob'

print counter
print miles
print name

# a = b = c = 1
# aa, bb, cc = 1, 2, 'runoob'

# 标准数据类型
# Number
print ('------------------------Number----------------------------')
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))

print(isinstance(a, int))

# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型。

print(5 + 4)
print(5 - 4)
print(5 * 4)
print(2 / 4)
print(2 // 4)
print(5 % 4)
print(5 ** 4)

# 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型
print ('------------------------Number----------------------------\n\n')

# String

print ('--------------------------String--------------------------')
str = 'Runoob'

print str
print(str[0:-1])
print(str[0])
print(str[2:5])
print(str[2:])
print(str * 2)
print(str + 'Test')
print('Run\noob')

print ('--------------------------String-------------------------\n\n')
# List
print ('-------------------------List---------------------------')

list = ['abcd', 786, 2.33, 'runoob', 'ssdsdf']
tinylist = [123, 'runoob']

print(list)
print(list[0])
print(list[2:-1])
print(list[1:3])
print(tinylist * 2)
print(list + tinylist)

list[0] = 233.555
print(list)

print ('-------------------------List---------------------------\n\n')
# Tuple
print ('---------------------------Tuple-------------------------')

tuple = ('abcd', 898, 22.32, 'runoob', 'uhku')
tinyTuple = ('a', 23)

print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tinyTuple * 2)
print(tuple + tinyTuple)



print ('-----------------------------Tuple-----------------------\n\n')
# Sets
print ('----------------------------Sets------------------------')

student = {'Tom', 'Jim', 'Mary', 'Tom'}

print student

print ('----------------------------Sets------------------------\n\n')
# Dictionary
print ('----------------------------------------------------')
print ('----------------------------------------------------\n\n')

