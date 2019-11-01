# Create all folder lists to create
#
# For Parent Folder
main_folder = ["System_Files", "Public_Files"]
#
# Inside System_Files Folder
system_folder = ["Error_Logs", "Data_Files"]
#
# Inside Public_Files Folders
public_folder = ["Excel_Billing"]
#
#
# Path of all folders and sub folders
#
path_system_folder = main_folder[0]
#
path_system_data_folder = f"{path_system_folder}/{system_folder[1]}"
path_public_folder = main_folder[1]
path_excel_billing_folder = f"{main_folder[1]}/{public_folder[0]}"
#
#
#
#
serial_number_file_name = "serial"
serial_number_file_path = f"{path_system_data_folder}/"
#
#
#
#
sheet_start_from = 3
#
#
#
#
client_data_list_format = ['name', 'address', 'products', 'advance', 'discount', 'notes']


