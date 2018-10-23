import math


def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(4, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False


def filter_prime_list(number_list):
    print(number_list.__len__())
    if number_list.__len__ == 0:
        print('数组里没有数字')
    else:
        prime_dic = {}
        for i in number_list:
            if is_prime(i):
                prime_dic[str(i)] = '素数'
            else:
                prime_dic[str(i)] = '非素数'
        print(prime_dic)


number_list = {1, 2, 3, 4, 5, 6, 67, 7, 78, 8}
filter_prime_list(number_list)

