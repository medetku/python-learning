from sys import argv

filename = argv[1]
filename2 = argv[2]
ignore = ["duplex", "alias", "configuration"]

with open(filename) as src, open(filename2, 'w') as dst:
    for line in src:
        for ignore_word in ignore:
            if line.startswith("!") or ignore_word in line:
                break
        else:
            dst.write(line)
