def add_everything_up(a, b):
    try:
        result = a + b
    except TypeError:
        return f'{a}{b}'
    else:
        return f'результат сложения: {result}'
    finally:
        print('функция выполнила свою работу')


print(add_everything_up('dfgh', 789))
print()
print(add_everything_up(67, 78.6))

