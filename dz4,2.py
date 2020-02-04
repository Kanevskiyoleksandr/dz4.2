def my_func():
    print(" Задать длинну списка ")
    a = int(input())
    print(" Задать максимальное значение в списке")
    b = int(input())
    from random import randint
    c = [randint(1, b) for i in range(a)]
    print(c)
    d = [e for e in c if e > 10]
    print("Больше 10", d)
my_func()