# from itertools import combinations

from utils.files import obtain_objects_dict, obtain_objects_list, pretty_print_dict

# szukamy sprzeczności na atrybutach,
# gdy występuje przechodzimy do następnego atrybutu
# 3 pętle
# wczytywanie systemu decyzyjnego z pliku


def sequential_covering(objects):
    pretty_print_dict(objects)


def main():
    sequential_covering(obtain_objects_dict("sys_dec"))


if __name__ == "__main__":
    main()
