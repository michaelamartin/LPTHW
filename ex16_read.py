from sys import argv

script, file_input = argv
txt = open(file_input)

print txt.read()
