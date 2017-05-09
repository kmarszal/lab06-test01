import unittest

from eternal.main import calculate, main

"""
Run with PYTHONPATH=. python tests/test_dummy.py
"""


class TestDummy(unittest.TestCase):

    def test_fun(self):
       # weekday = calculate(2001, 1, 3)
       # self.assertEqual(weekday, 2005)

        retcode = main(("--year", "2001", "--month", "1", "--day", "3"))
        self.assertEqual(retcode, 0)
        
        weekday1 = calculate(2017, 5, 9)
        self.assertEqual(weekday1, 1)
        
        weekday2 = calculate(-1, 2.3, 1.0e-14)
        self.assertEqual(weekday2, None)
        
        weekday3 = calculate("2017","1","9")
        self.assertEqual(weekday3, 0)
        
        weekday4 = calculate({2017,2018},1,2)
        self.assertEqual(weekday4, None)
        
        retcode1 = main((""))
        self.assertEqual(retcode1, 0)
        
        retcode2 = main(("--year", "0.0", "--MONTH", "1999", "--DaY", "[-2]"))
        self.assertEqual(retcode2, 0)

if __name__ == '__main__':
  unittest.main()
