# age = input()
# if 1 <= int(age) <= 120:
#     if int(age) % 10 == 1:
#         print(f"Вам {age} год.")
#     elif int(age) % 10 == 4 or int(age) % 10 == 3 or int(age) % 10 == 2:
#         print(f"Вам {age} года.")
#     else:
#         print(f"Вам {age} лет.")

age = int(input())
if 1 <= age <= 120:
    if age % 10 == 1:
        a = "Вам " + str(age) + " год."
    elif age % 10 == 4 or age % 10 == 3 or age % 10 == 2:
        a = "Вам " + str(age) + " года."
    else:
        a = "Вам " + str(age) + " лет."
    print(a.decode(encoding='UTF-8', errors='strict'))

