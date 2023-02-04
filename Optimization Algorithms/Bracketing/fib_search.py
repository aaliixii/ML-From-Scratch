def fib(n, memo):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fibonacciSearch(arr, target, offest, memo):

    n = len(arr)
    k = 0
    while True:
        if fib(k) >= n:
            break
        k+=1
    
    
    


def main():
    arr = []
    while True:
        try:
            arr.append(int(input('Enter a number.\nType q to quit')))
        except ValueError:
            break

    target = int(input('Target number:\n'))
    offset = -1
    idx = fibonacciSearch(arr, target, offset)
    
    if idx != -1:
        print(f'Found at idx: {idx}')
    else:
        print('Not Found')


if __name__ == '__main__':
    main()