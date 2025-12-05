name = input("Введите ваше имя: ")
age = int(input("Введите ваш возраст: "))

if age >= 18:
    is_adult = True
else:
    is_adult = False

print(f"Здравствуйте, {name}! Вам {age}. Совершеннолетний {is_adult}")
