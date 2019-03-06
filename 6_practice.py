#! usr/bin/python3
# Table printer

tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

col_width = [0] * len(tableData)

for i in range(len(col_width)):
    col_width[i] = col_width[i] + len(max(tableData[i], key=len))

for x in range(4):
    for i in range(len(tableData)):
        print(tableData[i][x].rjust(col_width[i]), end=' ')
    print()
