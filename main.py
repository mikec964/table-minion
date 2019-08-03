from dicetable import DiceTable

die_rolls = [7, 3, 5]
print(DiceTable.roll_on_tables('injury', die_rolls,
    show_table=True, show_roll=True))

die_rolls = [6 ,2, 1]
print(DiceTable.roll_on_tables('insult-pt1', die_rolls,
    show_table=False, show_roll=False))

