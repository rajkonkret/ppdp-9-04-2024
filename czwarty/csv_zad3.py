import pandas

# pi install pandas

data = pandas.read_csv('records3.csv', delimiter=";")
print(data)
#      name branch  year  cgpa
# 0   radek    coe     3   0.1
# 1   tomek    cos     3   0.1
# 2  michal    cod     3   0.1
# 3   zenek    cor     3   0.1

print(data.columns)
# Index(['name', 'branch', 'year', 'cgpa'], dtype='object')

print(data.values)
# [['radek' 'coe' 3 0.1]
#  ['tomek' 'cos' 3 0.1]
#  ['michal' 'cod' 3 0.1]
#  ['zenek' 'cor' 3 0.1]]

print(data.items)
# <bound method DataFrame.items of      name branch  year  cgpa
# 0   radek    coe     3   0.1
# 1   tomek    cos     3   0.1
# 2  michal    cod     3   0.1
# 3   zenek    cor     3   0.1>
