#SCRIPT START#
from netmiko import ConnectHandler
from getpass import getpass
import time 
from datetime import datetime

#device_name = input("Enter device name: ")
username = input("Enter username: ")
password = getpass()
listname = input ("Enter list name: ")
keyword = input ("Enter keyword: ")

subname = datetime.now().strftime("%Y%m%d-%H%M%S")


filename = "/REPORTS/show_int_descriptions/show_int_descriptions" + subname + ".csv" 

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
    output0 = net_connect.send_command('show run | inc hostname')
    output1 = net_connect.send_command('show int desc | inc ' + keyword )    
    
    print (output0[8:30])
    print (output1)
    
    time.sleep(1)
    file.write(output0[8:30])
    file.write('\n')
    file.write('\n')
    file.write(output1)
    file.write('\n')
    file.write('\n')
    time.sleep(3)
    
    net_connect.send_command('end\n')
    
    print ("Report saved to Reports directory...")
    time.sleep(1)
    #file.close()

#SCRIPT STOP#
