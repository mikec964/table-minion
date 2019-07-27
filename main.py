from dicetable import DiceTable

table1 = DiceTable('tables/injury.csv')
print(table1)

for roll in range(2, 13):
    print(roll, table1.lookup_roll(roll))
