from first_run import run_first_stage
from functions import get_serial_no, convert_to_dictionary
from values import serial_number_file_path as sl_p, serial_number_file_name as sl_n, client_data_list_format
from getdata import get_all_client_data
from create import CreateNewExcelFile

run_first_stage()

# # To get client Data
# client_data = get_all_client_data()
# dictionary = convert_to_dictionary(client_data, client_data_list_format)
# product_count = len(dictionary['products'])
sl = get_serial_no(sl_p, sl_n)
dictionary = {'name': 'Rudransh Jagannath', 'address': 'Tihu, Nalvari, Assam', 'products': [('Bhindi', 2.5), ('Pav Bhaji', 4.0), ('chole', 7.0), ('rajma', 5.0), ('dal makhani', 4.0), ('yellow dal', 6.5)], 'advance': 0, 'discount': 0, 'notes': ['Chole is hard and oily', 'Please cook the food well', 'Only the dehydration of your food is carried out']}
dictionary.update({'invoice no': sl})
dictionary.update({'date': '27/07/2019'})

obj = CreateNewExcelFile(dictionary)

