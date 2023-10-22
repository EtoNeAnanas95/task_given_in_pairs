import csv
import json
from dataclasses import dataclass
from Defs import Character, choose_option



# Дата класс для сейвов
@dataclass(slots=True, frozen=True)
class Save:
    name: str
    surname: str
    middle_name: str
    action: str


# Дата класс, который будет хранить юзернейм пользователя и все его сейвы
@dataclass(slots=True, frozen=True)
class User:
    username: str
    saves: list[Save]


# Сохранение персонажа
def save_character(character: Character) -> None:
    # Создаем массив для уже существующих сейвов (чтобы потом проверять существует ли он и добавлять/обновлять, если существует)
    existing_data = []

    try:
        # Открываем файл saves.csv только для чтения с кодировкой utf-8
        with open("saves.csv", "r", encoding="utf-8") as file:
            # Создаем csv.reader, который читает file
            reader = csv.reader(file)

            # Считываем заголовок csv, то есть первую строку
            header = next(reader)

            # Хз, как вкратце обьяснить. Но оно считывает заголовки в словарь, чтобы мы потом могли к ним обращаться и считывать конкретно по заголовкам
            header_dict = {header[i]: i for i in range(len(header))}

            for row in reader:
                existing_data.append(row)
    # Срабатывает если файл saves.csv не найден
    except FileNotFoundError:
        header_dict = {}
        existing_data = []

    # Создаем уникальный индентификатор, по которому будем сравнивать существует ли уже такой персонаж или нет, чтобы в будущем обновлять его и т.д.
    unique_identifier = (character.username, character.name, character.surname, character.middle_name)

    # Проходимся по массиву с уже существующей датой
    for row in existing_data:
        # Если username, name, surname, middle_name равен нашему уникальному индентификатору, то мы просто изменяем action нашего пользователя и выходим из цикла
        if (row[header_dict["username"]], row[header_dict["name"]], row[header_dict["surname"]],
            row[header_dict["middle_name"]]) == unique_identifier:
            row[header_dict["action"]] = character.action
            break
    else:
        # Иначе (если не найден пользователь с таким же индентификатором) мы добавляем нового персонажа и записываем всего данные
        existing_data.append(
            [character.username, character.name, character.surname, character.middle_name, character.action])

    # Открываем файл saves.csv для чтения с кодировокой utf-8
    with open("saves.csv", "w", newline="", encoding="utf-8") as file:
        # Создаем csv.writer для file
        writer = csv.writer(file)
        # Записываем заголовки
        writer.writerow(["username", "name", "surname", "middle_name", "action"])
        # Записываем обновленную информацию
        writer.writerows(existing_data)

# Сохранение инвентаря
def save_inventory(character: Character) -> None:
    # У нас в инвентаре имя хранится в виде массива (я уже говорил, что это для того, чтобы было проще сравнивать
    # Поэтому мы создаем такой же массив с именем того персонажа, которого нам передали в аргумент функции
    character_name = [character.surname, character.name, character.middle_name]

    try:
        # Открываем файл inventory.json только для чтения с кодировокй utf-8 и считываем все что есть в нашем inventory.json
        with open("inventory.json", "r", encoding="utf-8") as file:
            # Записываем его содержание в data
            data = json.load(file)
    # Срабатывает, если не найден файл или не удалось считать json
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        # Ставится пустой массив инвентарей, т.к. их там нет
        data = {"inventories": []}

    # Создаем булевую переменную для того, чтобы знать найден наш инвентарь или нет
    found = False

    # Проходимся по инвентарям
    for user_data in data["inventories"]:
        # Если username и name совпадает, то обновляем наш инвентарь и ставим, что он найден, а также выходим из цикла
        if user_data["username"] == character.username and user_data["name"] == character_name:
            user_data["inventory"] = character.inventory

            found = True
            break

    # Если инвентарь не был найден, то создаем новый и добавляем в массив inventories
    if not found:
        data["inventories"].append(
            {
                "username": character.username,
                "name": character_name,
                "inventory": character.inventory
            }
        )

    # Конвертируем каждый инвентарь в list (не знаю, насколько эта строчка важна и будет ли оно работать без нее, но оставляем)
    for user_data in data["inventories"]:
        user_data["inventory"] = list(user_data["inventory"])

    # Открываем inventory.json только для записи с кодировкой utf-8
    with open("inventory.json", "w", encoding="utf-8") as file:
        # Записываем в наш file наши инвенатри в data, а indent = 4 значит, что будет 4 таба (тип слева отступ), а ensure_ascii = False означает, что оно не будет конвертировать символы в коидровку и сохранит как они есть, то что нужно для работы с кириллицей
        json.dump(data, file, indent=4, ensure_ascii=False)


# Получаем всех пользователей
def load_users() -> list[User]:
    # Создаем пустой словарь
    users = {}

    # Открываем saves.csv только для чтения с кодировкой utf-8
    with open("saves.csv", mode="r", encoding="utf-8") as file:
        # Создаем csv.DictReader, который будет читать в наш файл
        reader = csv.DictReader(file)
        # Проходимся по каждому рдяу в файле
        for row in reader:
            # Получаем юзернейм
            username = row["username"]
            # Создаем сейв
            save = Save(row["name"], row["surname"], row["middle_name"], row["action"])

            # Если юзернейма нет в пользователях, то создаем нового пользователя с пустым масивом сохранений
            if username not in users:
                users[username] = User(username, [])

            # Добавляем нашему пользоователю сохранение
            users[username].saves.append(save)

    # Возвращаем массив с пользователями из saves.csv
    return list(users.values())

# Функция для ывбора пользователя и его сохранения, возвращает tuple (кортеж) с User и Save
def choose_save() -> tuple[User, Save]:
    # Получаем всех пользователей из функции выше
    users = load_users()

    # Спрашиваем у пользователя выбор, а в качестве выбора передаем массив [user.username} for user in users], который содержит просто username всех пользователей из saves.csv
    choosen = choose_option("Выберите пользователя: ", [user.username for user in users], clear=True,
                            is_string=False)

    # Получаем выбранного пользователя
    user = users[choosen]

    # Спрашиваем у пользователя выбор, а в качестве выбора передаем массив [f"{save.surname} {save.name} {save.middle_name}" for save in user.saves], который содержит просто имя всех персонажей в формете {Фамилия} {Имя} {Отчество} из saves.csv
    choosen = choose_option("Выберите сохранение: ",
                            [f"{save.surname} {save.name} {save.middle_name}" for save in user.saves], clear=True,
                            is_string=False)

    # Возвращаем выбранного пользователя и выбранный сейв
    return (user, user.saves[choosen])


# Загружаем инвентарь из json
def load_inventory(username: str, name: list[str]) -> list:
    # Открываем inventory.json только для чтения с кодировкой utf-8
    with open("inventory.json", "r", encoding="utf-8") as file:
        # Считываем весь json в переменную data
        data = json.load(file)

    # Проходимся по инвентарям
    for inventory in data["inventories"]:
        # Проверяем наш ли это инвентарь
        if inventory["name"] == name and inventory["username"] == username:
            # Возвращаем его
            return inventory['inventory']

    # Иначе возвращаем пустой массив
    return []
