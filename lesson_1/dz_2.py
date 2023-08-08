# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для проверки: «Число является простым, если делится нацело только на единицу и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

limit = 100000

while True:
    input_number = int(input("Введите целое число:\n"))
    if input_number < 0 or input_number > limit:
        print("Введите число в диапазоне от 0 до 100000")
    else:
        break

if input_number == 0 or input_number == 1:
    print("число", input_number, "является ни простым ни составным")
else:
    count = 0
    for i in range(1, input_number):
        if input_number % i == 0:
            count += 1
    if count >= 3:
        print("число", input_number, "является составным")
    else:
        print("число", input_number, "является простым")

