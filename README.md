# network-data-to-excel-file
A script to programmatically connect to network devices, collect information, and put them into an excel file.

## OBJECTIVE OF THE SCRIPT

The script connects to a network device, performs some 'show' commands to retrieve information (Port name, Speed, Duplex, Description, IP address, Mask) and generates an excel file with the collected data. This excel file can then be sent to other teams, archived, etc.

This script provides a solid base to build on to meet your needs. You can customize it as you wish.

The script will output something like this (by default):

![image](https://user-images.githubusercontent.com/104331973/190849660-b66b4c20-5513-4a96-80dc-255392f99a16.png)


## WHAT'S INSIDE

1) This script mainly uses the Netmiko library to connect to network equipment and issue commands.
Its versatility allows it to connect to any type of equipment: servers, routers, switches, firewalls, etc.

2) The TextFSM module will allow parsing the output of semi-formatted CLI commands into structured data. The data will be placed in data structures such as lists, dictionaries, etc. This allows its analysis and processing using common programming elements. Netmiko uses the TextFSM module.

3) Finally the module XlsxWriter, as its name indicates, allows you to generate and fill in Excel files from the data you provide.
Here it will be used to format our data and make them presentable, easily readable, and diffusable to other people even non-technical.

Now that we have stated the purpose of the program and what it does, let's move on to the technical part.

## PRE-REQUISITES

- Version Python 3.x.x
- Install the required packages from the 'requirements.txt file'
  - You can use 'pip install -r requirements.txt'

  
## LAUNCHING THE SCRIPT

After moving to the folder where the script is stored.

- From a Terminal:
  - python3 main.py $DEVICE_ADMINISTRATION_IP

- Exemple:
  - python3 main.py 10.1.1.1

The script need the device administration IP as an argument to connect.

After the end of the program, it will generate the excel file containing the researched data.
The excel filename correspond (by default) to the hostname of the router. It can be found on the same folder than the script.

## IMPROVEMENT

I tried to keep the script very basic so that it can be easily customizable and re-usable by anyone.

One way of improving this script could be, let's say if you have a huge number of devices to connect to, is to put those devices administration IP into a text file, and to modifiy the script to iterate through that text file line by line, catch the admin ip, and launch the script as a function sequentially.

Or maybe you want to put more date into the excel file, so you will likely do some more show commands to gather the particulars information you are looking for and activate some more cells in the excel file to write them.

You may also not want to put the login credentials in the script in clear text so you may want to input() those parameters in the program at runtime.

It really depends on you, but feel free to modify and adapt it to your needs. 
You can share it if you want and drop a comment, I will be more than happy to help :)
 
### SOURCES
 
Netmiko : https://pynet.twb-tech.com/blog/netmiko-python-library.html and https://github.com/ktbyers/netmiko

TextFSM Templates : https://github.com/networktocode/ntc-templates

XlsxWriter Documentation : https://xlsxwriter.readthedocs.io/
 
 
 
