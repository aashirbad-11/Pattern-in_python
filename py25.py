for i in range(1, 6):
    for j in range(5, 0,-1):
        if i >= j:
            print(str(i), end = '')
            print(' ', end = '')
        else:
            print('  ', end = '')
    print()

'''
        1 
      2 2 
    3 3 3 
  4 4 4 4 
5 5 5 5 5 

'''