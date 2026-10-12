counts = dict()
words_appeard = list()
filename = input('Enter a file name: ')
file = open(filename, 'r')


print('Counting.........')

for line in file:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        words_appeard.append(word)
print('Words',words_appeard)
print('Counts ', counts)