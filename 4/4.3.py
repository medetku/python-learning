config = "switchport trunk allowed vlan 1,3,10,20,30,100"
result = config.split()    
result = result[-1].split(',')
print(result)

