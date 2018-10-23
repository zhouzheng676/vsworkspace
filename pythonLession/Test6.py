import math

'''判断一个数字是否为素数'''


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


def my_debug(func):
    def wrapper(*args, **kwargs):
        print("使用的方法为:".format(func.__name__))
        print('传入的参数为：', *args)
        return func(*args, **kwargs)

    return wrapper  # 返回


@my_debug
def filter_prime_list(number_list):
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


if __name__ == '__main__':
    while True:
        input_number = input("请输入数字集合，输入Q或者q退出")
        if input_number == "q" or input_number == "Q":
            break
        else:
            prime_dictionary = []
            wrong_list = []
            number_list = input_number.split(',')
            if number_list.__len__() == 0:
                break
            else:
                for j in number_list:
                    if j != '':
                        try:
                            j = int(j)
                            prime_dictionary.append(j)
                        except ValueError:
                            wrong_list.append(j)
                filter_prime_list(prime_dictionary)
