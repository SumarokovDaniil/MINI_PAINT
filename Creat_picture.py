from additional_function import *
from Picture.square_not_full import square_not_full

mas_global = []


def create_mas(w, h, bg):
    """
    Создает главное поле для картинки в которое будут вписываться пикчи
    """
    global mas_global
    mas_global = [[] for _ in range(h)]
    for y in range(h):
        for x in range(w):
            mas_global[y].append(bg)


def prinal_islam(mas_picture):  # ну типа обрезает -______-
    """
    Запихивает картинкy в основной массив
    """
    global mas_global

    if ft_len(mas_picture[0]) >= ft_len(mas_global[0]) and ft_len(mas_picture) >= ft_len(mas_global):
        x_len = ft_len(mas_global[0])
        y_len = ft_len(mas_global)
        for y in range(y_len):
            for x in range(x_len):
                if mas_picture[y][x] != '':
                    mas_global[y][x] = mas_picture[y][x]
    elif ft_len(mas_picture[0]) >= ft_len(mas_global[0]) or ft_len(mas_picture) >= ft_len(mas_global):
        if ft_len(mas_picture[0]) >= ft_len(mas_global[0]):
            x_len = ft_len(mas_global[0])
            y_len = ft_len(mas_picture)
            for y in range(y_len):
                for x in range(x_len):
                    if mas_picture[y][x] != '':
                        mas_global[y][x] = mas_picture[y][x]
        else:
            x_len = ft_len(mas_picture[0])
            y_len = ft_len(mas_global)
            for y in range(y_len):
                for x in range(x_len):
                    if mas_picture[y][x] != '':
                        mas_global[y][x] = mas_picture[y][x]
    elif ft_len(mas_picture[0]) < ft_len(mas_global[0]) and ft_len(mas_picture) < ft_len(mas_global):
        x_len = ft_len(mas_picture[0])
        y_len = ft_len(mas_picture)
        for y in range(y_len):
            for x in range(x_len):
                if mas_picture[y][x] != '':
                    mas_global[y][x] = mas_picture[y][x]


create_mas(3, 6, '_')
xx = square_not_full(0, 0, 4, 4, '*')
prinal_islam(xx)
for x in range(len(mas_global)):
    print(*mas_global[x])
