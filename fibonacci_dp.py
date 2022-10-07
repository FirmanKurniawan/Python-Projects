def fib(n):
    if(n < 2):
        return n
    else:
        l = [0, 1]
        for i in range(2, n+1):
            l[i%2] = l[i%2] + l[(i+1)%2]
        return l[n%2]

if __name__ == '__main__':
    n = int(input('Enter a number: '))
    ans = fib(n)
    print(''.join(['Fib(', str(n), ') = ', str(ans)]))
