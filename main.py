from dicetable import DiceTable

table1 = DiceTable('tables/injury-h.csv')
print(repr(table1))
print(str(table1))

for roll in range(2, 13):
    print(f'Rolled a {roll}, got {table1.lookup_roll(roll)}')

