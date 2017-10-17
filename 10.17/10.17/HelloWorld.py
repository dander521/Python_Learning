#coding:utf-8

# 同一行显示多条语句
# import sys; x = 'runoob'; sys.stdout.write(x + '\n')
from sys import argv,path

print('path:',path)

# 单行注释
print("Hello, World!")

# 多行注释
# 多行注释
# 多行注释
print("Hello, Python!")

''' 换行注释
    换行注释 
'''
# 行与缩进
if True:
    print("True")
else:
    print("False")

# 多行语句
itemOne = 1
itemTwo = 2
itemThree = 3

total = itemOne + \
        itemTwo + \
        itemThree
print(total)

# 数据类型
# 1. 整数
# 2. 长整数
# 3. 浮点数
# 4.复数

# 字符串
word = '字符串'
sentence = "这是一个句子"
paragraph = """ 这是一个段落，
可以由多行组成"""

# 等待用于输入
# input("\n\n按下 enter 键后退出。")

# 多个语句构成代码组

a = 10

if a > 0:
    print(1)
elif a == 0:
    print(2)
else:
    print(3)


x='a'
y='b'

print(x)
print(y)

print('----------------')

print x, y
print y

# 在 python 用 import 或者 from...import 来导入相应的模块。
# 将整个模块(somemodule)导入，格式为： import somemodule
# 从某个模块中导入某个函数,格式为： from somemodule import somefunction
# 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
# 将某个模块中的全部函数导入，格式为： from somemodule import *

print ('=================Python import mode=====================')
print ('命令行参数为：')
for i in sys.argv:
    print i

print ('\n python 路径为\n ', sys.path)

