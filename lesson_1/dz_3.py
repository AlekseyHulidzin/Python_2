# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

lower_limit = 0
upper_limit = 1000
number_attempts = 10

while True:
    num_user = int(input("загадайте число:\n"))
    if num_user < lower_limit or num_user > upper_limit:
        print("Введите число в диапазоне от ", lower_limit, "до ", upper_limit)
    else:
        break

count = 0
num_bot = randint(lower_limit, upper_limit)

while count < number_attempts:
    count += 1

    print("попытка №", count, "от бота  число: ", num_bot)
    if num_bot == num_user:
        print("бот угодал число с количеством попыток: ", count)
        break
    elif num_bot > num_user:
        print("загаданное число меньше")
        upper_limit = num_bot
        num_bot = (lower_limit + upper_limit) // 2
    else:
        print("загаданное число больше")
        lower_limit = num_bot
        num_bot = (lower_limit + upper_limit) // 2
else:
    print("попытки бота исчерпаны, бот не угодал число")
    count = -1
