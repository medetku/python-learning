from sys import argv

filename = argv[1]
ignore = ["duplex", "alias", "configuration"]

with open(filename) as f:
    for line in f:
        for words in ignore:
            if line.startswith("!") or words in line:
                break
        else:
            print(line.rstrip())
