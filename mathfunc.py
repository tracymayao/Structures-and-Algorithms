import random


# Design add for large numbers,
# 大数加法

def big_add(x, y):
    (x_digits, y_digits) = convert_to_arr_for_add(x, y)
    # print(x_digits, y_digits)
    result = add_arr(x_digits, y_digits)
    return result
    # print("long_add", result)


def convert_to_arr_for_add(x, y):
    x_digits = []
    y_digits = []

    x_len = len(str(x))
    y_len = len(str(y))

    for i in range(x_len):
        x_digits.append(x // 10 ** (x_len - 1 - i))
        x %= 10 ** (x_len - 1 - i)

    for i in range(y_len):
        y_digits.append(y // 10 ** (y_len - 1 - i))
        y %= 10 ** (y_len - 1 - i)

    if (len(x_digits) > len(y_digits)):
        for i in range(len(x_digits) - len(y_digits)):
            y_digits.insert(0, 0)
    elif (len(y_digits) > len(x_digits)):
        for i in range(len(y_digits) - len(x_digits)):
            x_digits.insert(0, 0)
    else:
        x_digits.insert(0, 0)
        y_digits.insert(0, 0)

    return (x_digits, y_digits)


def add_arr(arr1, arr2):
    if len(arr1) != len(arr2):
        print("error at converting arrays")
    else:
        length = len(arr1)
        result_arr = []
        for i in range(length - 1, -1, -1):
            sum = arr1[i] + arr2[i]
            # print(i, sum)
            if (sum >= 10):
                inc = sum // 10
                # print("when sum is bigger than 10 inc is", inc)
                sum %= 10
                # print("when sum is bigger than 10 sum becomes" , sum)
                arr1[i - 1] += inc
            result_arr.insert(0, sum)

        result = 0
        for i in range(len(result_arr)):
            result += result_arr[i] * (10 ** (len(result_arr) - i - 1))

        return result


