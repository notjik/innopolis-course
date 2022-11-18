print("Попробуй угадать слово по буквам!")
secret_word = "машина"
attempts = 5
user_chars = []
for i in range(len(secret_word)):
    print("*", end=' ')
print()
while True:
    is_win = True
    print('Попыток: ' + str(attempts))

    user_char = input('Введите букву ')
    if user_char not in user_chars:
        user_chars.append(user_char)
    for char in secret_word:
        if char in user_chars:
            print(char, end=' ')
        else:
            print('*', end=' ')
            is_win = False
    print()
    if user_char not in secret_word:
        attempts -= 1
    if attempts == 0:
        print('Вы проиграли. Загаданное слово: ' + secret_word)
        break
    if is_win:
        print('Вы победили')
        break
