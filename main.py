from dicetable import DiceTable
import os

def roll_on_tables(first_table, die_rolls,
                    show_table=False, show_roll=True):
    t_name = first_table
    r_num = 0
    rText = ''
    while t_name != '':
        table = DiceTable(os.path.join('tests','tables', t_name) + '.csv')
        if show_table:
            rText += f'Checking {t_name}\n...'
        roll = die_rolls[r_num]
        r_num += 1
        if show_roll:
            rText += f'Rolled {roll}: '
        rText += f'{table.lookup_result(roll)}\n'
        t_name = table.lookup_next(roll)
    return rText

die_rolls = [7, 3, 5]
print(roll_on_tables('injury', die_rolls,
    show_table=True, show_roll=True))

die_rolls = [6 ,2, 1]
print(roll_on_tables('insult-pt1', die_rolls,
    show_table=False, show_roll=False))

