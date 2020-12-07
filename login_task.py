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
	host = input("Enter host: ")
	
    
	ios_device = {
    'device_type': 'cisco_ios',
    'ip': host, 
    'username': username,
    'password': password
     }
    
	net_connect = ConnectHandler(**ios_device)
	#output0 = net_connect.send_command('show run | inc hostname')
	#print (output0[10:40])   

loginTask()
