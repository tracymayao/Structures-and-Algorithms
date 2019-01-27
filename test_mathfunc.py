# -*- coding: utf-8 -*-
'''
大数加法UT
'''
import unittest
from mathfunc import *

class TestMathFunc(unittest.TestCase):
    """Test mathfuc.py"""

    # 使用大随机数测试大数加法
    big_x = 2 ** random.randint(32, 40)
    big_y = 2 ** random.randint(32, 50)

    big_sum = big_x + big_y
    big_add_result = big_add(big_x, big_y)

    print("Performing test using", big_x, "and", big_y)
    print("Python built-in add for adding big numbers result", big_sum)
    print("Big_Add adding big numbers result", big_add_result)
    if (big_sum == big_add_result):
        print(big_sum, "Equal to", big_add_result, "Big_Add test Passed")
    else:
        print("Big_Add test Failed")

if __name__ == '__main__':
    unittest.main()
