from netmiko import ConnectHandler

sshCli = ConnectHandler(
    device_type="cisco_ios",
    host="192.168.0.100",
    port=22,
    username="chacon1",
    password="edutek"
    )


output = sshCli.send_command("show ip arp")


print(output)
#este es un comentario
