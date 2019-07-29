import os
import sys
sys.path.append(os.path.abspath('..'))
import unittest

from dicetable import DiceTable

# You can run all tests in this directory with:
# python -m unittest discover -p '*tests.py'


class test_DiceTable(unittest.TestCase):

    def test_load_table(self):
        tables = ['injury', 'injury-guts', 'injury-head']
        for t in tables:
            t_path = 'tables/' + t + '.csv'
            print(t_path)
            t1 = DiceTable(t_path)
            self.assertEqual(t, t1.name)

    def test_1value(self):
        t1 = DiceTable('tables/injury.csv')
        self.assertEqual(t1.low[0], 2)
        self.assertEqual(t1.high[0], 2)
        self.assertEqual(t1.data[0], t1.lookup_result(2))

    def test_range(self):
        t1 = DiceTable('tables/injury.csv')
        self.assertEqual(t1.low[1], 3)
        self.assertEqual(t1.high[1], 4)
        self.assertEqual(t1.data[1], t1.lookup_result(3))
        self.assertEqual(t1.data[1], t1.lookup_result(4))

    def test_result(self):
        t1 = DiceTable('tables/injury.csv')
        self.assertEqual(t1.data[1], t1.lookup_result(3))
        
    def test_next(self):
        t1 = DiceTable('tables/injury.csv')
        self.assertEqual(t1.data[2], t1.lookup_result(5))
        self.assertEqual(t1.lookup_next(5), 'injury-guts')
        self.assertEqual(t1.data[1], t1.lookup_result(3))
        self.assertEqual(t1.lookup_next(1), '')

if __name__ == '__main__':
    unittest.main()
