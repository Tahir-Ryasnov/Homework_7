from function import decorator_logger

file_name = input('Введите имя текстового файла: ')

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


@decorator_logger(file_name)
def find_name():
    num_doc = input('Введите номер документа: ').strip()
    count = 0
    for file in documents:
        if num_doc in file.values():
            print(file.get('name'))
        else:
            count += 1
    if count == len(documents):
        print('В каталоге нет документа с таким номером')


@decorator_logger(file_name)
def myltiply(a, b, c):
    return a * b * c


if __name__ == '__main__':
    find_name()
    myltiply(2, 3, 4)
