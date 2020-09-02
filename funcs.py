from data.documents import documents
from data.directories import directories

def people_search():
    """Команда, которая спросит номер документа и выведет имя человека, которому он принадлежит"""
    print('\nВы вызвали команду для определения имени по номеру документа')
    id_number = input('Введите номер документа ')

    requested_name = None
    for user_data in documents:

        if user_data['number'] == id_number:
            requested_name = user_data['name']
            print(requested_name)
            return requested_name
    if requested_name == None:
        requested_name = 'Запись о человеке с данным документом отстуствует'
    print(requested_name)
    return requested_name


def shelf_search():
    """Команда, которая спросит номер документа и выведет номер полки, на которой он находится"""
    print('\nВы вызвали команду для поиска полки по номеру документа')

    id_number = input('Введите номер документа ')
    shelf = None
    for directory, docs in directories.items():
        if id_number in docs:
            shelf = directory
            print(f'Документ находится на {shelf}-й полке')
            return shelf
    if shelf == None:
        shelf = 'Данный документ отстуствует'

    return shelf


def docs_list():
    """Команда для вывода списка всех документов"""
    all_docs = []
    for user_data in documents:
        user_info = list(user_data.values())
        user_str = user_info[0] + ' "' + user_info[1] + '" "' + user_info[2] + '"'
        all_docs.append(user_str)
    print('Список всех документов каталоге')
    print(all_docs)
    return all_docs

def add_new_doc_input():
    """Команда для добавления нового документа в каталог и в перечень полок"""
    print('\nДобавление нового документа в каталог')
    new_user_doc = input('Введите тип документа ')
    new_user_id = input('Введите номер документа ')
    new_user_name = input('Введите имя владельца документа ')
    shelf_put = input('Укажите полку, на которой Вы разместите документ ')

    return add_new_doc(new_user_doc, new_user_id, new_user_name, shelf_put)

def add_new_doc(new_user_doc, new_user_id, new_user_name, shelf_put):

    new_user_dict = {}

    new_user_dict['type'] = new_user_doc
    new_user_dict['number'] = new_user_id
    new_user_dict['name'] = new_user_name

    documents.append(new_user_dict)

    def doc_to_shelf(shelf_put):

        shelves = list(directories.keys())
        if shelf_put not in shelves:
            print('Указанной полки нет в каталоге')
            shelf_put = input('Укажите полку, на которой Вы разместите документ ')
            return doc_to_shelf()
        else:
            docs_on_shelf = directories[shelf_put]
            docs_on_shelf.append(new_user_id)
            directories[shelf_put] = docs_on_shelf
            print(directories)
            return shelf_put

    doc_to_shelf(shelf_put)

    return f'документ {new_user_doc} {new_user_id} {new_user_name} был добавлен на  полку {shelf_put}'

def doc_delete_input():
    """Команда для удаления документа из каталога и из перечня полок по его номеру"""
    doc_to_be_del = input('\nВведите номер документа для удаления ')
    return doc_delete(doc_to_be_del)

def doc_delete(doc_to_be_del):

    docs_checklist = []
    for user_data in documents:
        docs_checklist.append(user_data['number'])
    if doc_to_be_del not in docs_checklist:
        print('Указанный документ отсутствует в каталоге')
        return doc_delete_input()
    else:
        for user_data in documents:
            if user_data['number'] == doc_to_be_del:
                documents.remove(user_data)


        for docs_in_directory in directories.values():

            if doc_to_be_del in docs_in_directory:
                docs_in_directory = docs_in_directory.remove(doc_to_be_del)
                return  f'Документ {doc_to_be_del} удалён'




def doc_to_move():
    """Команда для перемещения документа на целевую полку"""
    doc_to_be_moved = input('\nВведите номер документа для перемещения ')
    target_dict = input('Укажите на какую полку переместить документ ')

    shelves = list(directories.keys())
    if target_dict not in shelves:
        print('Указанной полки нет в каталоге')
        return

    docs_checklist = []
    for user_data in documents:
        docs_checklist.append(user_data['number'])
    if doc_to_be_moved not in docs_checklist:
        print('Указанный документ отсутствует в каталоге')
    else:
        for directory, docs in directories.items():
            if doc_to_be_moved in docs:
                docs = docs.remove(doc_to_be_moved)
                break
        directories[target_dict].append(doc_to_be_moved)
        print(directories)


def add_shelf():
    """Команда для размещения новой полки в кателоге"""
    new_shelf = input('\nУкажите номер новой полки для документов ')

    shelves = list(directories.keys())
    if new_shelf in shelves:
        print('Указанная полка уже есть в каталоге')
    else:
        directories[new_shelf] = []
        print('\nНовый список каталогов')
        print(directories)


def data_organizer():
    """
    p - Команда, которая спросит номер документа и выведет имя человека, которому он принадлежит
    s - Команда, которая спросит номер документа и выведет номер полки, на которой он находится
    l - Команда для вывода списка всех документов
    a - Команда для добавления нового документа в каталог и в перечень полок
    d - Команда для удаления документа из каталога и из перечня полок по его номеру
    m - Команда для перемещения документа на целевую полку
    as - Команда для размещения новой полки в кателоге
    """
    print('Добро пожаловать в интерфейс управления каталога документов. \nДля вызова списка команд введите !')
    while True:
        try:
            user_command = input('\nВведите команду для необходимого действия ')
            if user_command == 'p':
                people_search()
            elif user_command == 's':
                shelf_search()
            elif user_command == 'l':
                docs_list()
            elif user_command == 'a':
                add_new_doc_input()
            elif user_command == 'd':
                doc_delete_input()
            elif user_command == 'm':
                doc_to_move()
            elif user_command == 'as':
                add_shelf()
            elif user_command == '!':
                help(data_organizer)
            else:
                print('Неизвестная команда')
        except:
            break