from itertools import combinations

# 3 pętle
# wczytywanie systemu decyzyjnego z pliku


def pretty_print_dict(objects):
    print("     a1,  a2,  a3,  a4,  a5,  a6    d")
    for k, v in objects.items():
        print(k, v)


def obtain_objects_dict(fname):
    file = open(fname, "r")
    objects = dict()
    for i, line in enumerate(file.readlines(), start=1):
        objects[f"ob{i}"] = line.split()
    file.close()
    return objects


def obtain_objects_list(fname):
    file = open(fname, "r")
    objects = []
    for i, line in enumerate(file.readlines(), start=1):
        objects.append(line.split())
    file.close()
    return objects


def sequential_covering(objects):
    pretty_print_dict(objects)


def main():
    sequential_covering(obtain_objects_dict("sys_dec"))


if __name__ == "__main__":
    main()
