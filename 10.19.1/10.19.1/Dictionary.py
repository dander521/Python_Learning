#coding:utf-8
import sys

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

del dict['Name'] # 删除键 'Name'
dict.clear()     # 删除字典
del dict         # 删除字典

# a, b = 0, 1
# while b < 1000:
#     print(b, end=';')
#     a, b = b, a+b

list1 = [1, 2, 3, 4]
it = iter(list1)
print(next(it))
print(next(it))

print('-----------')

# for x in it:
#     print(x)

# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

def fabonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fabonacci(10)

while True:
    try:
        print(next(f), end=' ')
    except StopIteration:
        sys.exit()