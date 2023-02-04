def fib(n, memo):
    if memo[n] is not None:
        return memo[n]
    
    if n == 1 or n == 2:
        return 1
    else:
        result = fib(n - 1, memo) + fib(n - 2, memo)
        memo[n] = result
        return result

def main():
    n = int(input())
    memo = [None] * (n + 1)
    print(fib(n, memo))

if __name__ == '__main__':
    main()