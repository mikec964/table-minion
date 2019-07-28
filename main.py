from dicetable import DiceTable

table_paths = [ 'tables/injury.csv',
                'tables/injury-guts.csv',
                'tables/injury-head.csv'
                ]

table = {}
for path in table_paths:
    t = DiceTable(path)
    table[t.name] = t
    # if t1_name == '':
    #     t1_name = t.name
    # print(path)
    # print(str(table[t.name]))

def roll_on_tables(first_table, die_rolls,
                    show_table=False, show_roll=True):
    t_name = first_table
    r_num = 0
    rText = ''
    while t_name != 'NA':
        if show_table:
            rText += f'Checking {t_name}\n...'
        roll = die_rolls[r_num]
        r_num += 1
        if show_roll:
            rText += f'Rolled {roll}: '
        rText += f'{table[t_name].lookup_result(roll)}\n'
        t_name = table[t_name].lookup_next(roll)
    return rText

die_rolls = [7, 3, 5]
print(roll_on_tables('injury', die_rolls,
    show_table=True, show_roll=True))

