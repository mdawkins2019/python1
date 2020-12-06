from netmiko import ConnectHandler
from getpass import getpass
import time 
device_name = input("Enter device name: ")
username = input("Enter username: ")
 
HOST = device_name 
iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip':(HOST),
    'username': username,
    'password': getpass('Enter SSH password: '),
}

net_connect = ConnectHandler(**iosv_l2)

output1 = net_connect.send_command('show ip interface brief | inc down                  down')
output2 = net_connect.send_command('show ip interface brief | inc administratively down')


print (output1)
print (output2) 
time.sleep (90)     
net_connect.send_command('end\n')



