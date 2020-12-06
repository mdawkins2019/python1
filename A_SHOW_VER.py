#!/usr/bin/env python

from netmiko import ConnectHandler
from netmiko import ssh_exception
from paramiko.ssh_exception import AuthenticationException
from netmiko.ssh_exception import NetmikoAuthenticationException
from netmiko.ssh_exception import NetMikoTimeoutException
import sys
from getpass import getpass

device_name = input("Enter device name: ")
username = input("Enter username: ")

 
with open('/LISTS/REMOTE_DEP_SWITCHES_1.txt') as f:
    devices_list = f.read().splitlines()

for devices in devices_list:
    print ('Connecting to device ' + str(devices))
    ip_address_of_device = devices
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': ip_address_of_device, 
        'username': username,
        'password': password
    }

    try:
        net_connect = ConnectHandler(**ios_device)
    except (AuthenticationException):
        print ('Authentication failure: ' + str(ip_address_of_device))
        continue
    except (NetMikoTimeoutException):
        print ('Timeout to device: ' + str(ip_address_of_device))
        continue
    except (EOFError):
        print ("End of file while attempting device " + str(ip_address_of_device))
        continue
    except (SSHException):
        print ('SSH Issue. Are you sure SSH is enabled ? ' + str(ip_address_of_device))
        continue
    except Exception as unknown_error:
        print ('Some other error: ' + str(unknown_error))
        continue


output3 = net_connect.send_command('show run | inc hostname')
output = net_connect.send_command('show version | inc image')
output2 = net_connect.send_command('dir /all')
print (output3)
print (output) 
print (output2)
     
net_connect.send_command('end\n')



