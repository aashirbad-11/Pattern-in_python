n = 5
for i in range(1, n+1):
    for j in range(n-1, i-1, -1):
        print('  ', end = '')
    for k in range(1, i+1):
        print(str(k), end = '')
        print(' ', end = '')
    print()
'''

        1 
      1 2 
    1 2 3 
  1 2 3 4 
1 2 3 4 5 
'''