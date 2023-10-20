from game import *
import os
import csv

current_directory = os.getcwd()
file_path = os.path.join(current_directory, 'save.csv')

if os.path.exists(file_path):
    with open(file_path, mode="r") as file:
        reader = csv.reader(file)
        menu(reader)
else:
    with open("save.csv", "w", newline="") as file:
        writer = csv.writer(file)
    user_name = str(input("Введите имя пользователя: "))
    character = character()
    game_moment = game(character)

game()
