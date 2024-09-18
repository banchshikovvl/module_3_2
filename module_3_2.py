# Создайте функцию send_email, которая принимает 2 обычных аргумента:
# сообщение и получатель и 1 обязательно именованный аргумент со значением по умолчанию - отправитель.

# Внутри функции реализовать следующую логику:
# Проверка на корректность e-mail отправителя и получателя.
# Проверка на отправку самому себе.
# Проверка на отправителя по умолчанию.

# Создайте функцию send_email, которая принимает 2 обычных аргумента:
# message(сообщение), recipient(получатель) и 1 обязательно именованный аргумент со значением по умолчанию
# sender = "university.help@gmail.com".
# Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net",
# то вывести на экран(в консоль) строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
# Если же sender и recipient совпадают, то вывести "Нельзя отправить письмо самому себе!"
# Если же отправитель по умолчанию - university.help@gmail.com,
# то вывести сообщение: "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
# В противном случае вывести сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>."
# Здесь <sender> и <recipient> - значения хранящиеся в этих переменных.
# За один вызов функции выводится только одно из перечисленных уведомлений! Проверки перечислены по мере выполнения.

def send_email(message, recipient, sender='university.help@gmail.com'):
    list_ = ['.com', '.ru', '.net']
    if '@' in recipient and '@' in sender and any(i in recipient for i in list_) and any(i in sender for i in list_):
        if recipient == sender:
            print('Нельзя отправить письмо самому себе!')
        elif sender == 'university.help@gmail.com':
            print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        else:
            print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')


send_email('Здравствуйте', 'jony.gmail.com')
print(' ')
send_email('Здравствуйте', 'jony@.gmail.co')
print(' ')
send_email('Здравствуйте', 'jony@.gmail.com', 'ivanov@gmail.ru')
print(' ')
send_email('Здравствуйте', 'jony@.gmail.com')
print(' ')
send_email('Здравствуйте', 'jony@.gmail.com', 'jony@.gmail.com')
