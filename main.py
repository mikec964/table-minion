from dicetable import DiceTable

table1 = DiceTable('tables/injury-h.csv')
print(table1.__repr__())
print(table1)

for roll in range(2, 13):
    print(f'Rolled a {roll}, got {table1.lookup_roll(roll)}')


# print(parse_next_table('two /rollon(hi)'))
