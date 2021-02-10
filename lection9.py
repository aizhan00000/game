# пользователь вводит целое число - программа должна найти сумму чисел от нуля до данного числа,
# а также найти произведение чисел от одного до данного числа. программа должна вывести на экран полученную сумму
# и произведение а также колличество слагаемых в сумме и кол-во множителей в произведегии
#

def get_sum(a):
    count = 0
    sum_of_nums = 0
    for i in range(0, a+1):
        sum_of_nums += i
        count += 1
    return sum_of_nums, count


def get_multiple(a):
    count = 0
    multiple_of_num = 1
    for i in range(0, a+1):
        multiple_of_num *= i
        count += 1

    return multiple_of_num, count









