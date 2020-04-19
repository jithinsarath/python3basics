#simple febonacci printing
def febonacci(num):
    a = 0
    b = 1

    print(a)
    print(b)

    for i in range(num-2):
        c = a + b
        a = b
        b = c
        print(c)

febonacci(200)
