# 作业一：

# 区分以下类型哪些是容器序列哪些是扁平序列，哪些是可变序列哪些是不可变序列：

# list
# tuple
# str
# dict
# collections.deque
# 作业二：
# 自定义一个 python 函数，实现 map() 函数的功能。

# 作业三：
# 实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。

# --------------------------------------------------------------------------------




# question_1

# 容器序列：list、tuple、collections.deque ，能存放不同类型的数据容器序列可以存 放不同类型的数据
# 扁平序列：str ，存放的 是相同类型的数据扁平序列只能容纳一种类型。
# 可变序列：list、dict、collections.deque 
# 不可变序列：tuple、str 

# 列表
l = []
l.append(123)
l.append(True)
l.append('aksd')
print(l)

# 元组
t = (123,True,'asdjf')
print(t)

# 容器的双向队列
from collections import deque
c_d = deque('uvw')
c_d.append(123)
c_d.appendleft(True)
print(c_d)

# 字典
d = {}
d['123'] = 123
d['abc'] = 'abc'
d['boolean'] = True
print(d)


# question_2

# map(函数，序列) 将序列中每个值传入函数，处理完成返回为map 对象 
# number = list(range(11)) 
# def square(x): return x**2 
# print(list(map(square, number))) 
# print(dir(map(square, number))) 


def sque_1(parameter_list):
    return parameter_list**3
m = map(sque_1, range(10))
next(m)
list(m)
[sque_1(parameter_list) for parameter_list in range(10)]






# question_3

import time
def timer(func):
    def inner3(*args,**kwargs):
        t1 = time.time()
        func(*args,**kwargs)
        t2 = time.time()
        print('函数执行时间为：',t2 - t1)
    return inner3

@timer
def mul_tab(a,b,c):
    print(a**b**c+b**a**c+a**c**b+b**c**a)
    
mul_tab(3,3,5)
