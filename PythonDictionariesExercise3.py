filename = input('Enter a file name: ')
senders = dict()
try:
    file = open(filename, 'r')
except FileNotFoundError:
    exit('File does not exist.')


for line in file:
    if line.startswith('From') and len(line.split()) == 7:
        words = line.split()
        email = words[1]
        senders[email] = senders.get(email, 0) + 1


print(senders)