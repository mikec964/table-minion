import csv
import os


class DiceTable():
    ''' Returns results from table based on die roll

    low[row], high[row], result[row]
    '''

    def __init__(self, f_path):
        self.name = os.path.splitext(os.path.basename(f_path))[0]
        with open(f_path) as f:
            cr = csv.reader(f)
            self.data = []
            self.low = []
            self.high = []
            for row in cr:
                ranger = row[0].split('-')
                self.low.append(ranger[0])
                if len(ranger) > 1:
                    self.high.append(ranger[1])
                else:
                    self.high.append(ranger[0])
                self.data.append(row[1])


    def lookup(self, dieroll):
        pass


table1 = DiceTable('tables/injury.csv')
print(f'===== {table1.name} table =====')
print('| low | high | result ')
print('|-----|------|--------')
for row in range(len(table1.data)):
    print(f'| {table1.low[row]} | {table1.high[row]} | {table1.data[row]}')

