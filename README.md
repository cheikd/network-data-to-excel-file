# network-data-to-excel-file
A script to programmatically connect to network devices, collect information, and put them into an excel file.

OBJECTIVE OF THE SCRIPT

The script connects to a network device (CISCO), performs some 'show' commands to retrieve information (Port name, Speed, Duplex, Description, IP address, Mask) and generates an excel file with the collected data. This excel file can then be sent to other teams, archived, etc.

This script provides a solid base to build on to meet your needs. You can customize it as you wish.

The script will output something like this (by default):

![image](https://user-images.githubusercontent.com/104331973/190848158-5568406f-1f74-4d99-8a43-4b540f02cece.png)


WHAT'S INSIDE

1) This script mainly uses the Netmiko library to connect to network equipment and issue commands.
Its versatility allows it to connect to any type of equipment: servers, routers, switches, firewalls, etc.

2) The TextFSM module will allow parsing the output of raw CLI commands output into structured data. The data will be placed in data structures such as lists, dictionaries, etc. This allows its analysis and processing using common programming elements. Netmiko uses the TextFSM module.

3) Finally the last important module is XlsxWriter. This module, as its name indicates, allows you to generate and fill in Excel files from the data you provide.
Here it will be used to format our data and make them presentable, easily readable, and diffusable to other people even non-technical.

Now that we have stated the purpose of the program and what it does, let's move on to the technical part.

PRE-REQUISITES

- Python 3.x.x
- Install the required packages from the 'requirements.txt file'
  You can use 'pip install -r requirements.txt'

  
LAUNCHINT THE SCRIPT

python3 main.py $DEVICE_ADMINISTRATION_IP

Exemple:
python3 main.py 10.1.1.1

The script takes the device administration as an argument.

After the program have finished it will generate the excel file containing the information we were looking for. 
The Excel filename correspoond by default to the hostname of the router. It can be found on the same execution folder were the script lives.

IMPROVEMENT
I tried to make the script very basic so that it can be easily customizable and re-usable by anyone.
One way of improving this script if you have a huge number of devices to connect to, is to put those devices administration ip into a txt file, and to modifiy the script to iterate through that text file catch, the admin ip and launch the script as a function sequentially.

Also Maybe you want to put more date into the excel file, so you will likely do some more show commands to gather the particulat date you are looking for and some more fieds in the excel file to write them.

It really depends on you, but feel free to modify and adapt it to your needs. Feel free to share it if you want also or drop a comment if it has helped you in anyway :)
 
 
