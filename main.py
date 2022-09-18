#by Cheik Diawara
#main program

from netmiko import Netmiko
from netmiko import ConnectHandler
from netmiko import NetMikoAuthenticationException
from netmiko import NetMikoTimeoutException
from pprint import pprint
import time
import platform
import sys

from generate_excel_file import generate_excel_file

# Intialization of time, to calculate execution time
start = time.time()

# Part 1 - Connect to the router, retrieve raw data and process it

# Looking for an argument
try:
    if sys.argv[1]:
        router_ip = sys.argv[1]
        router_user = 'cisco'
        router_password = 'cisco'

except IndexError:
    print("Need to provide the device administration IP as an argument.")
    exit()


print(f"\n{'#'*50}\n Connection to the router... \n{'#'*50}")

try:
    net_connect = ConnectHandler(
        device_type="cisco_ios_ssh", #To use Telnet change this parameter to "cisco_ios_telnet"
        host=router_ip,
        username=router_user,
        password=router_password,
    )

    print(net_connect.find_prompt())

    print(f"\n{'~'*50}\n Connected to the router!\n{'~'*50}")

# Commands to be executed on the router
    cmd_show_version = "show version"
    cmd_sh_ip_int_brief = "show ip int brief"
    cmd_sh_interfaces_description = "show interfaces description"
    cmd_sh_interfaces = "show interfaces"

# Retrieve Hostname and IOS version in dict from TestFSM
    print(f"\n{'~'*50}\nOn {net_connect.find_prompt()} Execution of the command: {cmd_show_version}\n{'~'*50}")
    router_output_cmd_show_version = net_connect.send_command(cmd_show_version, use_textfsm=True)

    router_version=router_output_cmd_show_version[0]["version"]

    router_hostname=router_output_cmd_show_version[0]["hostname"]

    pprint(router_output_cmd_show_version) # outputed to terminal for debugging purposes


# Retrieve interface name
    print(f"\n{'~'*50}\nOn {net_connect.find_prompt()} Execution of the command: {cmd_sh_ip_int_brief}\n{'~'*50}")
    router_output_cmd_sh_ip_int_brief = net_connect.send_command(cmd_sh_ip_int_brief, use_textfsm=True)

    pprint(router_output_cmd_sh_ip_int_brief) # outputed to terminal for debugging purposes

    router_interface_name_list=[]

    for dict_item_intf_name in router_output_cmd_sh_ip_int_brief:
        router_interface_name_list.append(dict_item_intf_name["intf"])


# Retrieve Interface Description
    print(f"\n{'~'*50}\nOn {net_connect.find_prompt()} Execution of the command: {cmd_sh_interfaces_description}\n{'~'*50}")
    router_output_sh_interfaces_description = net_connect.send_command(cmd_sh_interfaces_description, use_textfsm=True)

    pprint(router_output_sh_interfaces_description) # outputed to terminal for debugging purposes

    router_description_name_list=[]

    for dict_item_intf_desc in router_output_sh_interfaces_description:
        router_description_name_list.append(dict_item_intf_desc["descrip"])

# Retrieve Interface speed, duplex, and IP address
    print(f"\n{'~'*50}\nOn {net_connect.find_prompt()} Execution of the command: {cmd_sh_interfaces}\n{'~'*50}")
    router_output_cmd_sh_interfaces = net_connect.send_command(cmd_sh_interfaces, use_textfsm=True)

    pprint(router_output_cmd_sh_interfaces) # outputed to terminal for debugging purposes

    router_interfaces_speed_list=[]
    router_interfaces_duplex_list=[]
    router_ipaddress_list=[]

    for dict_item_intf in router_output_cmd_sh_interfaces:
        router_interfaces_speed_list.append(dict_item_intf["speed"])
        router_interfaces_duplex_list.append(dict_item_intf["duplex"])
        router_ipaddress_list.append(dict_item_intf["ip_address"])

except NetMikoAuthenticationException:
    print("Authentication problem encountered...")
    exit()

except NetMikoTimeoutException:
    print("A timeout occured during connection...")
    exit()

print(f"\n{'#'*50}\nRetrieval and processing of values on the router completed.\n{'#'*50}")


# Part 2 - Send results to the excel file generator function

print(f"\n{'#'*50}\nGenerating the excel file...\n{'#'*50}")

result_gen_excel_file=generate_excel_file(router_hostname,router_version,router_interface_name_list,router_ipaddress_list,
                                        router_description_name_list,router_interfaces_speed_list,router_interfaces_duplex_list)

end = time.time()
total_time = end - start

if result_gen_excel_file[0]=="OK":
    print ("Excel File Generated:",result_gen_excel_file[1])
    print(f"\n{'#'*50}\n End of programme, no error. \n Total execution time: {round(total_time,3)} seconds.\n{'#'*50}")
else:
    print ("The programme did not finish correctly.")
    print(f"\n{'#'*50}\n End of the programme, WITH ERROR!!!!  \n{'#'*50}")
