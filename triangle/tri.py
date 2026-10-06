import time
def tri(num,turn):
    d = 1
    turn = turn + 1


    while d != turn:
        print('disisisiisisi  :',d)

        if d % 2 == 0:
            for i in range(num):
                row = ''
                for j in range(i + 1):
                    row += '*'
                    print('\r' + row, end='', flush = True)
                    time.sleep(0.5)
                print() # move to the next line
        else:
            for i in range(num):
                row = ''
                for j in range(i + 1):
                    row += '#'
                    print('\r'+ row, end='', flush = True)
                    time.sleep(0.5)
                print()   # move to the next line

        d += 1

        # Move cursor back up by `num` lines
        if d != turn:
            print(f'\033[{num}A', end='', flush=True)

    return None


if __name__ == '__main__':
    num = 5
    ans = tri(num,3)
    print(ans)