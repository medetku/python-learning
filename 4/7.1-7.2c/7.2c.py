from sys import argv

ignore = ["duplex", "alias", "Current configuration"]

filename1, filename2 = argv[1:]

with open(filename1) as src, open(filename2, 'w') as dst:
    for line in src:
        for ignore_word in ignore:
            if line.startswith("!") or ignore_word in line:
                break
        else:
            dst.write(line)
