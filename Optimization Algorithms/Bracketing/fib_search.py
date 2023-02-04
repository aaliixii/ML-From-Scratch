def fib(x, memo):
    if memo[x] is not None:
        return memo[x]

    if x<=2:
        return 1
    else:
        result = fib(x-1, memo) + fib(x-2, memo)
    memo[x] = result
    return result

def fib_search(arr, n, x):
    k = 0
    fibM = 0
    memo = [None] * (n + 1)

    while True:
        if fib(k, memo) >= n:
            fibM = fib(k, memo)
            break
        k+=1

    fibMm1 = fib(k-1, memo)
    fibMm2 = fib(k-2, memo)

    



def main():
    x = int(input('Target:\n'))
    arr = []
    while True:
        try:
            arr.append(int(input('Enter number into Array.\tType q to quit\n')))
        except ValueError:
            break
    fib_search(arr, len(arr), x)
    return
    found, idx = fib_search(arr, len(arr), x)
    if found:
        print(f'Target Found in Array at {idx}')
    else:
        print('Target Not Found')

if __name__ == '__main__':
    main()