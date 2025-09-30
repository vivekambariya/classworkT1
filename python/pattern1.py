#         *
#         * *
#         * * *
#         * * * *

for i in range(4):
    for j in range(i+1):
        print('*', end=' ')
    print()
print(end='')
print(    )
#         * * * *
#         * * *
#         * *
#         *
for i in range(4):
    for j in range(4-i):
        print('*', end=' ')
    print()

#           *
#         * *
#       * * *
#     * * * *
print(end='')
print(    )
for i in range(4):
    for j in range(3-i):
        print(' ', end=' ')
    for k in range(i+1):
        print('*', end=' ')
    print()
#           *
  #       * * *
 #      * * * * *
#     * * * * * * *
print(end='')                   
print(    )
for i in range(4):
    for j in range(3-i):
        print(' ', end=' ')
    for k in range(i+1):
        print('*', end=' ')
    for l in range(i):
        print('*', end=' ')
    print()
print(end='')
print(    )
#           *
#         *   * 
#       *   *   * 
#     *   *   *   *
#   *   *   *   *   *
#     *   *   *   * 
#       *   *   *
#         *   *
#           *
for i in range(4):
    for j in range(4-i):
        print('', end=' ')
    for k in range(i+1):
        print('*', end=' ')
    print()

for i in range(5,0,-1):
    for j in range(5-i):
        print('', end=' ')
    for k in range(i):
        print('*', end=' ')
    print()
print(end='')
print(    )

for i in range(4):
    for j in range(4-i):
        print('', end=' ')
    for k in range(i+1):
        if i%2==0:
            print('*', end=' ')
        else:
            print('#', end=' ')
    print()
for i in range(5,0,-1):
    for j in range(5-i):
        print('', end=' ')
    for k in range(i):
        if i%2==0:
            print('*', end=' ')
        else:
            print('#', end=' ')
    print()

#           *
#         #   # 
#       *   *   * 
#     #   #   #   #
#   *   *   *   *   *
#     #   #   #   #
#       *   *   *
#         #   # 
#           *