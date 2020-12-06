import sys
from getpass import getpass
import time 
from datetime import datetime
from pprint import pprint 
from netmiko import ConnectHandler
from netmiko import ssh_exception
from paramiko.ssh_exception import AuthenticationException
from netmiko.ssh_exception import NetmikoAuthenticationException
from netmiko.ssh_exception import NetMikoTimeoutException

def loginTask():
	
	username = input("Enter username: ")
	password = getpass()
	listname = input ("Enter list name: ")

	subname = datetime.now().strftime("%Y%m%d-%H%M%S")

	filename = "/REPORTS/show_model_number/show_model_number" + listname + subname + ".csv" 

	print ("Writing output to REPORTS directory...")
	time.sleep(1)

	file = open(filename , 'w')

	with open("/LISTS/" + listname + ".txt") as f:
		devices_list = f.read().splitlines()


	for devices in devices_list:
		print ('Connecting to device ' + devices)
    
		HOST = devices
		ios_device = {
        'device_type': 'cisco_ios',
        'ip': HOST, 
        'username': username,
        'password': password
    }

		try:
			net_connect = ConnectHandler(**ios_device)
		except (AuthenticationException):
			print ('Authentication failure: ' + HOST)
			continue
		except (NetMikoTimeoutException):
			print ('Timeout to device: ' + HOST)
			continue
		except (EOFError):
			print ('End of file while attempting device ' + HOST)
			continue
		except (SSHException):
			print ('SSH Issue. Are you sure SSH is enabled? ' + HOST)
			continue
		except Exception as unknown_error:
			print ('Some other error: ' + str(unknown_error) )
			continue      
loginTask()
