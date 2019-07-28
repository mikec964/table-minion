from dicetable import DiceTable

table_paths = [ 'tables/injury-h.csv',
                'tables/injury-guts.csv',
                'tables/injury-head.csv'
                ]
die_rolls = [7, 3, 5]

table = {}
t1_name = ''
for path in table_paths:
    t = DiceTable(path)
    table[t.name] = t
    if t1_name == '':
        t1_name = t.name
    print(path)
    print(str(table[t.name]))

t_name = t1_name
r_num = 0
while t_name != 'NA':
    print('Rolling on', t_name)
    roll = die_rolls[r_num]
    r_num += 1
    print(f'...Got a {roll}: {table[t_name].lookup_roll(roll)[0]}')
    t_name = table[t_name].lookup_roll(roll)[1]

