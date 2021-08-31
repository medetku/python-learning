mac = "AAAA:BBBB:CCCC"
bin_mac = bin(int(mac.replace(":", ""), 16))
bin = bin_mac[2:]
print(bin)
