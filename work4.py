documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def find_document_owner(doc_number):
    for doc in documents:
        if doc['number'] == doc_number:
            return doc['name']
    return None


def handle_command_p():
    doc_number = input('Введите номер документа: ')
    owner = find_document_owner(doc_number)
    if owner:
        print(f'Владелец документа: {owner}')
    else:
        print('Документ не найден.')


def main():

    while True:
        command = input('Введите команду: ')
        if command == 'q':
            print('Программа завершена.')
            break
        elif command == 'p':
            handle_command_p()
        else:
            print('Неизвестная команда. Используйте "p" для поиска владельца документа или "q" для выхода.')


if __name__ == '__main__':
    main()
