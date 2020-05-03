s = 1
n = 5
for i in range(s, n + 1):
    for j in range(n -1, i -1, -1):
        print("  ", end ='')
    for k in range(1, i + 1):
        print(chr(k + 64), end ='')
        print(' ', end = '')
    print()


    '''

        A 
      A B 
    A B C 
  A B C D 
A B C D E


'''