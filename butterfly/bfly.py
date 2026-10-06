import time

def simpleRectange(n):
    for i in range(n):
        print(n * '*')


def rectangleNew(n):
    for i in range(n):
        for j in range(n):
            print('*', end=' ')
        print()

def triangle(n):
    for i in range(n):
        for j in range(i+1):
            print('*', end = ' ')
        print()

def invertedTriangle(n):
    for i in range(n):
        for j in range(n-i):
            print('*', end = ' ')
        print()


# turn/ times & speed
def butterFly(n, t, s):
    turn = 0
    SW = True
    SX = False

    while turn != t:

        for i in range(n):
            row = ''
            for j in range(i + 1):
                row += "* " if SW == True else "0 "
                # row += '* '
                print('\r\033[2K' + row, end='', flush=True)
                time.sleep(s)
                # SW = False

            for k in range(n - i - 1):
                row += '  '
                print('\r\033[2K' + row, end='', flush=True)

            for j in range(n - i - 1):
                row += '  '
                print('\r\033[2K' + row, end='', flush=True)

            for k in range(i + 1):
                # row += ' 0'
                row += "* " if SX == True else "0 "
                print('\r\033[2K' + row, end='', flush=True)
                time.sleep(s)
                # SX = False

            print()


        for i in range(n - 1):
            row = ''
            for j in range(n - i - 1):
                row += "* " if SW == True else "0 "
                # row += '* '
                print('\r\033[2K' + row, end='', flush=True)
                time.sleep(s)
                # SW = False

            for k in range(i + 1):
                row += '  '
                print('\r\033[2K' + row, end='', flush=True)

            for j in range(i + 1):
                row += '  '
                print('\r\033[2K' + row, end='', flush=True)

            for k in range(n - i - 1):
                # row += ' 0'
                row += "0 " if SX == False else "* "
                print('\r\033[2K' + row, end='', flush=True)
                time.sleep(s)
                # SX = True
            print()



        if SW == True:
            SW = False
        else:
            SW = True

        if SX == False:
            SX = True
        else:
            SX = False

        # print("SW: ",SW)
        # print("SX: ",SX)

        # Move back to the beginning of the triangle
        print(f'\033[{2*n-1}A', end='', flush=True)

        # Clear every line of the previous triangle
        for _ in range(2*n-1):
            print('\033[2K', end='', flush = True)
            print('\033[1B', end='', flush = True)

        # Move back to the beginning
        print(f'\033[{2*n-1}A', end='', flush=True)

        turn += 1

    # if t != turn:
    #     # Move back to the beginning of the triangle
    #     print(f'\033[{n}A', end='', flush=True)
    #
    #     # Clear every line of the previous triangle
    #     for _ in range(n):
    #         print('\033[2K', end='')
    #         print('\033[1B', end='')
    #
    #     # Move back to the beginning
    #     print(f'\033[{n}A', end='', flush=True)

    # print(SW)
    # print(SX)



# after loop











if __name__ == '__main__':
    # simpleRectange(4)
    # rectangleNew(4)
    # triangle(3)
    # invertedTriangle(4)
    t= 4
    butterFly(6,20,0.2)




