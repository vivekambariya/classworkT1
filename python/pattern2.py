for i in range(5):
    for j in range(5-i):
        print('*', end=' ')
    for k in range(i):
        print(''*2, end='  '*2)
    for l in range(5-i):
        print('*', end=' ')    
    print()
for i in range(5):
    for j in range(i+1):
        print('*', end=' ')
    for k in range(4-i):
        print(' '*2, end=' '*2)
    for l in range(i+1):
        print('*', end=' ')    
    print()
'''
* * * * * * * * * * 
* * * *     * * * * 
* * *         * * *
* *             * *
*                 *
*                 *
* *             * *
* * *         * * *
* * * *     * * * *
* * * * * * * * * *
'''
print(end=' ')
print( )
for row in range(10) :
    for col in range(10):
        if col== 0 or col== 9 or col== row or col== 9-row:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

print(end=' ')
print( )
'''
*                 *
* *             * *
*   *         *   *
*     *     *     *
*       * *       *
*       * *       *
*     *     *     *
*   *         *   *
* *             * *
*                 *
'''
for row in range(10) :
    for col in range(10):
        if (col== 0 or col== 9) or  ((col==1 or col== 8) and (row!=4 and row!=5)) or ((col==2 or col== 7) and (row<3 or row>6)) or ((col==3 or col== 6) and (row<2 or row>7)) or ((col==4 or col== 5) and (row==0 or row==9)):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()    
print(end=' ')
print( )
'''
* * * * * * * * * *
* * * *     * * * *
* * *         * * *
* *             * *
*                 *
*                 *
* *             * *
* * *         * * *
* * * *     * * * *
* * * * * * * * * *
'''
print(end=' ')
print( )
for row in range(7):
    for col in range(4):

        if col == 0:
            print('*', end=' ')
       
        elif (row == 0 or row == 3 or row == 6) and col < 3:
            print('*', end=' ')
       
        elif col == 3 and (row > 0 and row < 3):
            print('*', end=' ')
       
        elif col == 3 and (row > 3 and row < 6):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
'''
* * *
*     *
*     *
* * *
*     *
*     *
* * *
'''
print(end=' ')
print( )