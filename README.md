# network-data-to-excel-file
A script to programmatically connect to network devices, collect information and put them into an excel file.

WHAT THE PROGRAM DOSE EXACTLY

WHAT THE PROGRAM IS MADE OF

Now that we have stated the purpose of the program and what it does, let's move on to the technical part.

PRE-REQUISITES

- Python 3.x.x
- Install the required packages from the 'requirements.txt file'
  You can use 'pip install -r requirements.txt'
  
STARTING THE PROGRAM

python3 main.py $DEVICE_ADMINISTRATION_IP

exemple:
python3 main.py 10.1.1.1

The script takes the device administration as an argument.

After the program have finished it will generate the excel file containing the information we were looking for. 
The Excel filename correspoond by default to the hostname of the router. It can be found on the same execution folder were the script lives.

IMPROVEMENT
I tried to make the script very basic so that it can be easily customizable and re-usable by anyone.
One way of improving this script if you have a huge number of devices to connect to, is to put those devices administration ip into a txt file, and to modifiy the script to iterate through that text file catch, the admin ip and launch the script as a function sequentially.

Also Maybe you want to put more date into the excel file, so you will likely do some more show commands to gather the particulat date you are looking for and some more fieds in the excel file to write them.

It really depends on you, but feel free to modify and adapt it to your needs. Feel free to share it if you want also or drop a comment if it has helped you in anyway :)
 
 
