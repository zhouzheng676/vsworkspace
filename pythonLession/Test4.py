import math
import re


def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0: 
                return False
        return True
    return False


flag = 1
while flag:
    numa = input("请输入：")
    # 判断是否为正整数
    if re.match("^[+]?[0-9]*$", numa, 0):
        result = is_prime(int(numa))
        print('是素数' if(result) else '不是素数')
    # 判断是否为小数
    elif re.match("^[+-]?([0-9]{1,}[.][0-9]*)$", numa, 0):
        print('这是一个小数,请重新输入')
    # 判断是否为负数
    elif re.match("^-[0-9]*$", numa, 0):
        print('这是一个负数,请重新输入')
    else:
        print('unKnown输入,请重新输入')
