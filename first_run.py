from functions import check_folders, get_serial_no, back, goto
from values import *

check_folders(main_folder)

goto(path_system_folder)
check_folders(system_folder)
back()

goto(path_public_folder)
check_folders(public_folder)
back()

get_serial_no(serial_number_file_path, serial_number_file_name)



















