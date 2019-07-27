import csv
import os


class DiceTable():
    ''' Returns results from table based on die roll

    low[row], high[row], result[row]
    '''

    def __init__(self, f_path):

        def parse_range(range_str):
            ranger = range_str.split('-')
            low = int(ranger[0])
            if len(ranger) > 1:
                high = int(ranger[1])
            else:
                high = int(ranger[0])
            return [low, high]

        def parse_next_table(command_str):
            tResult = command_str
            tNext = 'NA'
            n = len('/rollon')
            if '/rollon' in command_str:
                start = command_str.find('/rollon(')
                end = command_str.find(')', start)
                tResult = command_str[:start-1] + command_str[end+1:]
                tNext = command_str[start+1+n:end]
            return [tResult, tNext]

        self.data = []
        self.low = []
        self.high = []
        self.next_table = []
        self.name = os.path.splitext(os.path.basename(f_path))[0]
        with open(f_path) as f:
            cr = csv.reader(f)
            for row in cr:
                tLow, tHigh = parse_range(row[0])
                self.low.append(tLow)
                self.high.append(tHigh)
                tResult, tNext = parse_next_table(row[1].strip())
                self.data.append(tResult)
                self.next_table.append(tNext)


    def __repr__(self):
        t = f'{self.name}\n'
        for row in range(len(self.data)):
            t += f'{self.low[row]},{self.high[row]},{self.data[row]},'
            t += f'{self.next_table[row]}\n'
        return t

    def __str__(self):
        t = f'===== {self.name} table =====\n'
        t += '| low | high | result \n'
        t += '|-----|------|--------\n'
        for row in range(len(self.data)):
            t += f'| {self.low[row]} | {self.high[row]} | {self.data[row]}\n'
        return t

    def lookup_roll(self, dieroll):
        tResult = 'NA'
        tNext = 'NA'
        for row in range(len(self.data)):
            if (dieroll >= self.low[row]) and dieroll <= self.high[row]:
                tResult = self.data[row]
                tNext = self.next_table[row]
        return [tResult, tNext]

