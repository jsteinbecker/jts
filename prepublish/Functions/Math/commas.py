'Underscores dont mess with int values'
n_1 = 2_000_000
n_2 = 3_500_000

ans = n_1 + n_2

'f-string comma int formatter'
print ( f'{ans:,}' )