from os import listdir, curdir, mkdir, rename, chdir
from num2words import num2words


def check_folders(list_of_folders):
    list_of_current_folders = listdir(curdir)

    for folder in list_of_folders:
        if folder in list_of_current_folders:
            print(f"{folder} Folder Found")
        else:
            mkdir(folder)
            print(f"{folder} Folder Created")


def get_serial_no(file_path, file_name):
    sl_f_name = [f"{file_path}{file_name}.bak", f"{file_path}{file_name}.txt"]
    try:
        rename(sl_f_name[0], sl_f_name[1])
        print("File Found")
    except FileNotFoundError:
        print("File Not Found")
        file = open(sl_f_name[1], "w")
        file.write("1")
        file.close()
        print("New File Created")
    finally:
        file = open(sl_f_name[1], "r")
        line = file.readline()
        serial_no = int(line)
        file.close()

        file = open(sl_f_name[1], "w")
        file.write(str(serial_no + 1))
        file.close()

        rename(sl_f_name[1], sl_f_name[0])
    return serial_no


def back(limit=1):
    for i in range(limit):
        chdir("..")


def goto(path):
    chdir(path)


def text_value_of(number, prefix="Rs.", suffix="Only"):
    word = num2words(number)
    word = f'{prefix} {word.replace(",", "").replace("-", " ").title()} {suffix}'
    return word


def convert_to_dictionary(data, index):
    c_d_d = {}
    n = 0
    for i in index:
        c_d_d.update({i: data[n]})
        n += 1
    return c_d_d
