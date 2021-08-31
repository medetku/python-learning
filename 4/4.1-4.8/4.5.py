command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"
commands = command1.split()
commands3 = command2.split()
result1 = commands[-1].split(',')
result2 = commands3[-1].split(',')
set(result1)
set(result2)
set1 = set(result1)
set2 = set(result2)
result1 = set1 & set2
result = list(result1)
print(result)
