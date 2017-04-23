'''
Write a python script that takes a list of lists of strings and displays it in a well-organized table with each column right-justified. Assume that all the inner lists will contain the same number of strings. For example, the value could look like this:


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
Your script would print the following:


  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose
  
'''

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

col_width = []
for lst in tableData:
    m = max([len(lst[i]) for i in range(len(lst))])
    col_width.append(m)

for i in range(len(tableData[0])):
    for j in range(len(tableData)):
        print(tableData[j][i].rjust(col_width[j]), end=' ')
    print()

