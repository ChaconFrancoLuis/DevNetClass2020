from netmiko import ConnectHandler
from getpass import getpass 
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import NetMikoAuthenticationException
from paramiko.ssh_exception import SSHException

Lista_IPS = open('routers.txt')
for IP in Lista_IPS:
    Conexion_equipo = {
        'device_type': 'cisco_ios',
        'ip':   IP,
        'username': 'Chacon1',
        'password': 'edutek',
    }

    print ('\n Connecting to the Device ' + IP.strip() + '\n')
    try:
        net_connect = ConnectHandler(**Conexion_equipo)
    except NetMikoTimeoutException:
        print ('Device not reachable' )
        continue

    except NetMikoAuthenticationException:
        print ('Authentication Failure' )
        continue

    except SSHException:
        print ('Make sure SSH is enabled' )
        continue

    output = net_connect.send_config_from_file(config_file='router_changes.txt',cmd_verify=False)
    print(output)

    print('\n Saving the Router configuration \n')
    output = net_connect.save_config()
    print(output)

    output = net_connect.send_command('show ip int brief')
    print(output)

