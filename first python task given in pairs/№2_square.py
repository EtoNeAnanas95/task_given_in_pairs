def rectangle_area(width, height):
    square = width * height
    return square
try:
    width = int(input("Введите ширину: "))
    height = int(input("Введите высоту: "))
    square = rectangle_area(width, height)
    print(f"площадь: {square}")
except ValueError:
    print("Введите данные нормально")
#цензурные анекдоты кончились(
#пока анекдотов больше не будет