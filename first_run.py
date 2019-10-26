from functions import check_folders, back, goto
from values import *


def run_first_stage():
    check_folders(main_folder)

    goto(path_system_folder)
    check_folders(system_folder)
    back()

    goto(path_public_folder)
    check_folders(public_folder)
    back()


















