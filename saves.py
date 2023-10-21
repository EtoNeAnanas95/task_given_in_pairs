from dataclasses import dataclass
from Defs import Character, choose_option
import json
import csv


@dataclass(slots=True, frozen=True)
class Save:
    name: str
    surname: str
    middle_name: str

    action: str


@dataclass(slots=True, frozen=True)
class User:
    username: str
    saves: list[Save]


def save_character(character: Character) -> None:
    existing_data = []

    try:
        with open("saves.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)

            header = next(reader)
            header_dict = {header[i]: i for i in range(len(header))}

            for row in reader:
                existing_data.append(row)
    except FileNotFoundError:
        header_dict = {}
        existing_data = []

    unique_identifier = (character.username, character.name, character.surname, character.middle_name)

    for row in existing_data:
        if (row[header_dict["username"]], row[header_dict["name"]], row[header_dict["surname"]], row[header_dict["middle_name"]]) == unique_identifier:
            row[header_dict["action"]] = character.action
            break
    else:
        existing_data.append([character.username, character.name, character.surname, character.middle_name, character.action])

    with open("saves.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["username", "name", "surname", "middle_name", "action"])
        writer.writerows(existing_data)

def save_inventory(character: Character) -> None:
    character_name = [character.surname, character.name, character.middle_name]

    try:
        with open("inventory.json", "r", encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = {"inventories": []}

    found = False

    for user_data in data["inventories"]:
        if user_data["username"] == character.username and user_data["name"] == character_name:
            user_data["inventory"] = character.inventory

            found = True
            break

    if not found:
        data["inventories"].append(
            {
                "username": character.username,
                "name": character_name,
                "inventory": character.inventory
            }
        )

    for user_data in data["inventories"]:
        user_data["inventory"] = list(user_data["inventory"])

    with open("inventory.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


# возвращает лист с юзерами тип юзерс типо элементы в листе все будут юзерс ю ноу ну а че те не ясно тада
def load_users() -> list[User]:
    users = {}
    with open("saves.csv", mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            username = row["username"]
            save = Save(row["name"], row["surname"], row["middle_name"], row["action"])
            if username not in users:
                users[username] = User(username, [])
            users[username].saves.append(save)

    return list(users.values())


def choose_save() -> tuple[User, Save]:
    users = load_users()

    choosen = choose_option("Выберите пользователя: ", [f"{user.username}" for user in users], clear=True, is_string=False)
    user = users[choosen]

    choosen = choose_option("Выберите сохранение: ", [f"{save.surname} {save.name} {save.middle_name}" for save in user.saves], clear=True, is_string=False)

    return (user, user.saves[choosen])

def load_inventory(username: str, name: list[str]) -> list:
    with open("inventory.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    for inventory in data["inventories"]:
        if inventory["name"] == name:
            return inventory['inventory']

    return []