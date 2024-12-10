def send_mail(message, recipient, sender='univercite.help@gmail.com'):
    if '@' not in recipient or '@' not in sender or not sender.endswith(('.com', '.ru', '.net')) or not recipient.endswith(('.com', '.ru', '.net')):
        print('Невоозможно отправить с адреса {} на адрес {}'.format(sender, recipient))
    elif sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    else:
        print('Письмо отправленно успешно: Отправитель: {}, Получатель: {}, Сообщение: {}'.format(sender, recipient, message))

message = 'Привет! Как дела?'
recipient = 'friend@gmail.com'
sender = 'me@gmail.com'


send_mail(message, recipient, sender)