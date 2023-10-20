from dataclasses import dataclass
from Defs import Character
from json import load, dumps

@dataclass(slots=True, frozen=True)
class Save:
    name: str
    surname: str
    middle_name: str

    inventory: set
    action: str


def save_character(character: Character) -> None:
    ...


def save_inventory(character: Character) -> None:
    with open("inventory.json", "w+") as inventory:
        json = load(inventory)

        if 'inventories' in json:
            ...
        else:
            json["inventories"] = []
            json["inventories"] = json["inventories"].append(
                {
                    "username": character.username,
                    "inventory": list(inventory)
                }
            )

            inventory.write(dumps(json))




def load_saves() -> list[Save]:
    ...