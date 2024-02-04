def fibo(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        n_first = 0
        n_second = 1
        print(n_first, n_second, end=" ")
        for i in range(2, n + 1):
            result = n_first + n_second
            print(result, end=" ")
            if i == n:
                print()
                print(f'{n} элемент последовательности Фибоначчи = {result}')

            n_first = n_second
            n_second = result


n = int(input('Введите число: '))
fibo(n)
