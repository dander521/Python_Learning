#coding:utf-8

from fibo import fib, fib2

vec = [2, 4, 6]

print([3*x for x in vec if x != 2])

for i in range(4):
    print(i)

a = {x for x in 'abracadabra' if x not in 'abc'}

print(a)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

fib(12)

