ip = "192.168.3.1"
ip1 = ip.split(".")
ip2 = """
{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}"""
print(ip2.format(int(ip1[0]), int(ip1[1]), int(ip1[2]), int(ip1[3])))
