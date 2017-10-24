#coding:utf-8

# 操作系统接口

import os

print(os.getcwd())

import glob

# os.chdir('/Users/geeker/Documents/Github/Python_Learning/10.24/10.24')
print(glob.glob('*.py'))

import sys

print(sys.argv)

sys.stderr.write('Warning, log file not found starting a new one\n')

import re

print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))

print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))


import math

math.cos(math.pi / 4)
math.log(1024, 2)

import random

random.choice(['apple', 'pear', 'banana'])

random.sample(range(100), 10)   # sampling without replacement

random.random()    # random float

random.randrange(6)    # random integer chosen from range(6)

from urllib.request import urlopen

# for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
#     line = line.decode('utf-8')  # Decoding the binary data to text.
#     if 'EST' in line or 'EDT' in line:  # look for Eastern Time
#         print(line)

import smtplib

# server = smtplib.SMTP('localhost')
# server.sendmail('123020990@qq.com')
# server.quit()

from datetime import date
import datetime

now = date.today()
print(now)

datetime.date(2017, 10, 24)
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

birthday = date(1989, 7, 23)
age = now - birthday
print(age.days)

import zlib

s = b'hf jks h f sdfs ndvjn oeiv n ovnei odfkj hsdu hfuhf hsdkf h akjdh fla kjs dh'
print(len(s))

t = zlib.compress(s)
print(len(t))

print(zlib.decompress(t))

print(zlib.crc32(s))

from timeit import Timer

print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
print(Timer('a,b = b,a', 'a=1; b=2').timeit())

