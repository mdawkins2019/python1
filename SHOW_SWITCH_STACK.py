#SCRIPT START#
from netmiko import ConnectHandler
from getpass import getpass
import time 
from datetime import datetime
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException

#device_name = input("Enter device name: ")
username = input("Enter username: ")
password = getpass()
listname = input ("Enter list name: ")                 ##enter specific text list of devices that you want to connect to must be a .txt file. The .txt extension is not needed just the list name###
#keyword = input ("Enter keyword: ")
#reportname = input ("Enter report name: ") 

subname = datetime.now().strftime("%Y%m%d-%H%M%S")


filename = "/REPORTS/show_switch_stack/show_switch_stack_" + listname + subname + ".csv" #Customize this line to output specific report tp specific directory###

print ("Writing output to REPORTS directory...")
time.sleep(1)

file = open(filename , 'w')

with open("/LISTS/" + listname + ".txt") as f:
    devices_list = f.read().splitlines()


for devices in devices_list:
    print ('Connecting to device ' + devices)
    #ip_address_of_device = devices
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
    output0 = net_connect.send_command('show run | inc hostname')        ##This command used to list out the name of the device that you are connecting too##
    
    
    output1 = net_connect.send_command('show switch')
    output2 = net_connect.send_command('show switch stack-ports summary')
    output3 = net_connect.send_command('show switch stack-mode')
    output4 = net_connect.send_command('show switch neighbors ')
    
    
    
    print('\n')
    print (output0[8:35])
    print('\n')
    print(HOST)
    print('\n')
    print (output1)
    print('\n')    
    print (output2)
    print('\n')
    print (output3)
    print('\n')
    print (output4)
    time.sleep(1)
    
    
    time.sleep(1)
    
    file.write('\n')
    file.write(output0[8:35])
    file.write('\n')
    file.write(HOST)
    file.write('\n')
    file.write (output1)
    file.write('\n')
    file.write (output2)
    file.write('\n')
    file.write (output3)
    file.write('\n')
    file.write (output4)
    
    file.write('\n')
    file.write('\n')
    time.sleep(3)
    
    net_connect.send_command('end\n')
    
    print ("Report saved to Reports directory...")
    time.sleep(1)
    #file.close()

#SCRIPT STOP#
