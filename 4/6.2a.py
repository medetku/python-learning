ip_address = input("введите ip-адрес: ")
octets = ip_address.split('.')
ip = len(octets) == 4
for i in octets:
    ip = i.isdigit() and 0  <= int(i) <= 255 and ip
if ip:
    if 1 <= int(octets[0]) <= 223:
        print('unassigned')
    elif 224 <= int(octets[0]) <= 239:
        print('multicast')
    elif ip_address == '255.255.255.255':
        print('local broadcast')
    elif ip_address == '0.0.0.0':
        print('unassigned')
    else:
        print('unused')
else:    
    print("Неправильный IP-адрес")    
