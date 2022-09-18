#by Cheik Diawara
#module - generate excel file

import xlsxwriter
import time
import os
import itertools

def generate_excel_file(router_hostname,router_version,router_interface_name_list,router_ipaddress_list,
                        router_description_name_list,router_interfaces_speed_list,router_interfaces_duplex_list):

    print("Starting the write function...")

    excel_filename=router_hostname+".xlsx"

# Small Check optional. It checks if the file already exists in the folder and if yes, it supresses it.
    if os.path.exists(excel_filename):
        os.remove(excel_filename)
        print("The file has been deleted successfully")
        time.sleep(1)
        print("Creating the file...")
    else:
        print("The file does not exist!")
        print("Creating the file...")

    print("Writing on the excel file...")

# Create workbook and add worksheet.
    workbook = xlsxwriter.Workbook(excel_filename, {'strings_to_numbers': True})
    worksheet = workbook.add_worksheet(router_hostname)

# Create cells type for titles and important words
    cell_format = workbook.add_format({'bold': True, 'bg_color': 'yellow','italic':True})
    cell_format_bold = workbook.add_format({'bold': True, 'italic':True})
    cell_format_dev_blue = workbook.add_format({'bg_color': '#8BEEFF'})
    cell_format_align = workbook.add_format()
    cell_format_align.set_align('center')

# Adjust column width
    worksheet.set_column('A:A', 25)
    worksheet.set_column('B:B', 20)
    worksheet.set_column('C:C', 20)
    worksheet.set_column('D:D', 35)
    worksheet.set_column('E:E', 50)

#Titles and static values
    worksheet.write('A1','DEVICE NAME', cell_format)
    worksheet.write('B1','IOS VERSION', cell_format)

    worksheet.write('A6','Interfaces', cell_format)
    worksheet.write('B6','Speed', cell_format)
    worksheet.write('C6','Duplex', cell_format)
    worksheet.write('D6','IP Address/Mask', cell_format)
    worksheet.write('E6','Description', cell_format)

#Filling the file with information
    row = 6
    col_port_name = 0
    col_speed = 1
    col_duplex = 2
    col_ip_address = 3
    col_port_desc = 4

    for port_name, speed, duplex, ip_address, port_desc in zip(router_interface_name_list, router_interfaces_speed_list,
                                                                router_interfaces_duplex_list,router_ipaddress_list,
                                                                router_description_name_list):
        worksheet.write(row, col_port_name, port_name)
        worksheet.write(row, col_speed, speed)
        worksheet.write(row, col_duplex, duplex)
        worksheet.write(row, col_ip_address, ip_address)
        worksheet.write(row, col_port_desc, port_desc)
        row += 1

# General values
    worksheet.write('A2',router_hostname)
    worksheet.write('B2',router_version)

# Insert python logo
    worksheet.insert_image('D1', 'python-powered-w-200x80.png')

    workbook.close()

    print("End of the write function")

    return "OK", excel_filename
