#SCRIPT START#
from netmiko import ConnectHandler
from getpass import getpass
import time 
from datetime import datetime
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException


username = input("Enter username: ")
password = getpass()
listname = input ("Enter list name: ")


subname = datetime.now().strftime("%Y%m%d-%H%M%S")


filename = "/REPORTS/stack_ping/stack_ping_check" + listname + subname + ".csv" 

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
    output0 = net_connect.send_command('show run | inc hostname')
    output1 = net_connect.send_command('ping 10.101.200.100 source vlan 300 repeat 20 size 1500 ' ) 
    output2 = net_connect.send_command('ping 10.102.95.6 source vlan 320 repeat 20 size 1500' )
    output3 = net_connect.send_command('ping 10.10.61.61 source vlan 310 repeat 20 size 1500' )
    output4 = net_connect.send_command('ping 10.99.201.1 source vlan 2160 repeat 20 size 1500' )
    
    str1 = "% Invalid source interface - IP not enabled or interface is down"
    
         
    print ('**** ' + (output0[8:35]) + ' ****')
    print (output1)
    print ('\n')
    
    if output2 == str1:
	    print('Wireless vlan is not active')
    else: 
	    print(output2)
    print ('\n')
    
    if output3 == str1:
	    print('Voice vlan is not active')
    else: 
	    print(output3) 
    print ('\n')
    
     if output4 == str1:
	    print('Voice vlan is not active')
    else: 
	    print(output4) 
    print ('\n')
    
    time.sleep(1)
    file.write('**** ' + (output0[8:35]) + ' ****')
    file.write('\n')
    file.write('\n')
    file.write(output1)
    file.write('\n')
    file.write('\n')
    
    if output2 == str1:
	    file.write('Wireless Vlan is not active')
    else: 
	    file.write(output2)
    file.write('\n')
    file.write('\n')
    time.sleep(1)
    
    if output3 == str1:
	    file.write('Voice Vlan is not active')
    else: 
	    file.write(output3)
    file.write('\n')
    file.write('\n')
    file.write('\n')
    file.write('\n')
    time.sleep(1)

    if output4 == str1:
	    file.write('Voice Vlan is not active')
	    
	    
    else: 
	    file.write(output4)
    file.write('\n')
    file.write('\n')
    file.write('\n')
    file.write('\n')
    time.sleep(1)
    
    net_connect.send_command('end\n')
    
    print ("Report saved to Reports directory...")
    time.sleep(1)
    #file.close()


