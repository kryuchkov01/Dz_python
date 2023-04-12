# №8.1[49]. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .csv
# Информация о человеке:
# Фамилия, Имя, Телефон, Описание
# Корректность и уникальность данных не обязательны.
# Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода.
# Выберите наиболее удобную структуру данных для хранения справочника.
# 2) CRUD: Create, Read, Update, Delet
# Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
# Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека. Берем первое совпадение по фамилии.
# Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
# Delete: Удаление записи из справочника. Выбор - как в Read.
# 3) экспорт данных в текстовый файл формата csv
# 4) импорт данных из текстового файла формата csv
# Используйте функции для реализации значимых действий в программе
# Усложнение.
# - Сделать тесты для функций
# - Разделить на model-view-controller

#сделать update и delete!!!!!


fio = {1: {'surname':'Иванов', 'name':'Иван', 'number':'89234145', 'discrip':'работник'}}

phonebook = {}
phonebook_last_id = 0

def create(db: dict, id: int, surname: str, name: str, phone: str, discrip: str)-> tuple:
    db[id] = {'surname': surname, 'name': name, 'phone': phone, 'discrip': discrip}
    id += 1
    return db, id

def read(db: dict, surname_filter: str) -> int:
    for _id in db:
        if surname_filter.lower() in db[_id]['surname'].lower():
            return _id

def update(rec: dict, new_rec: str):
    pass
    # tmp_rec = new_rec.fromkeys(new_rec.keys())
    # for key in new_rec.keys():
    #     tmp_rec[key] = new_rec[key] if new_rec[key] != "" else rec[key]
    # return tmp_rec

def delete(db: dict, id: int, surname: str, name: str, phone: str, discrip: str):
    pass
 
def print_record(db: dict, _id: int):
    # if _id is not None:
        print(f'{"="*30}\n{db[_id]}\n{"="*30}\n')
    # else: print(f'{"="*30}\nЗапись не найдена.\n{"="*30}\n')

def get_user_data() -> tuple:
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    discrip = input('Введите описание: ')
    return surname, name, phone, discrip

def get_surname() -> str:
    surname = input('Введите искомую фамилию > ')
    return surname


def print_data(db: dict) -> None:
    for _id, data in db.items():
        print(f"[{_id}: {data['surname']} | {data['name']} | {data['phone']} | {data['discrip']} ]")

#3) экспорт данных в текстовый файл формата csv       

def export_db(db: dict, filepath: str, delimeter: str = '#') -> None:
    with open(filepath, mode = "w", encoding="utf-8") as file:
        for _id, data in db.items():
            file.write(f"{data['surname']}{delimeter}{data['name']}{delimeter}{data['phone']}{delimeter}{data['discrip']}\n")

def get_file_name() -> str:
    return input('Введите имя файла: s')

# 4) импорт данных из текстового файла формата csv ПОКА ЧТО НЕ РАБОТАЕТ, НЕТ ФАЙЛА data.txt

def import_db(db: dict, last_id: int, filepath: str, delimeter: str = '#') -> tuple:
    with open(filepath, mode = "r", encoding="utf-8") as file:
        for line in file:
            _data = line.strip().split(delimeter)
            db[last_id] = {'surname': _data[0], 'name': _data[1], 'phone': _data[2], 'discrip':_data[3]}
            last_id += 1
    return db, last_id   

def menu(db : dict, last_id: int) -> None:
    while True:
        print('Возможные действия: ')
        print('1. Создать запись ')
        print('2. Вывести имеющиеся данные ')
        print('3. Обновить запись ')
        print('4. Экспортировать данные в файл')
        print('5. Импортировать данные из файла ')
        print('6. Найти пользователя ')
        print('7. Выход ')
        user_input = input('Введите действия > ')
        if user_input == "1":
            record = get_user_data()
            db, last_id = create(db, last_id, *record)
        elif user_input == "2":
            print_data(db)
        # elif user_input == "3":
        #     to_change = read(db, get_surname())

        elif user_input == "4":
            export_db(db, get_file_name())
        elif user_input == "5":
            # db, last_id = import_db(db, last_id, get_file_name())
            db, last_id = import_db(db, last_id, 'data08_1.txt')
        elif user_input == "6":
            found_id = read(db, get_surname())
            try:
                print_record(db, found_id)
            except KeyError: 
                print(f'{"="*30}\nЗапись не найдена.\n{"="*30}\n')
        else:
            break

menu(phonebook, phonebook_last_id)
