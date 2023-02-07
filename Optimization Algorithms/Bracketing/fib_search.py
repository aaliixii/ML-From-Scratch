def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fibonacciSearch(arr, target, offest):

    n = len(arr)
    k = 0
    while True:
        if fib(k) >= n:
            break
        k+=1

    fk = fib(k)
    fk1 = fib(k - 1)
    fk2 = fib(k - 2)
    while fk2 >= 0:
        index = min(offest + fk2, n - 1)
        if arr[index] < target:
            fk = fk1
            fk1 = fk2
            fk2 = fk - fk1
            offest = index
        
        elif arr[index] > target:
            fk = fk2
            fk1 = fk1 - fk2
            fk2 = fk - fk1
        else:
            return index

    if arr[offest+1] and fk1 == target:
        return offest + 1
    return -1

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