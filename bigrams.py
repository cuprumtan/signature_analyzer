import math
import os


def count_all_bigrams(file):
    return os.path.getsize(file) - 1


def count_current_bigram(bigram, file):
    content = open(file, 'rb').read()
    return content.count(bigram)


if __name__ == '__main__':

    test_files = os.listdir('test')
    test_files = ['test' + '\\' + x for x in test_files]

    bigrams_dict = {}
    for x in range(0, 256):
        for y in range(0, 256):
            bigrams_dict[(x).to_bytes(1, byteorder='big') + (y).to_bytes(1, byteorder='big')] = 0

    for file in test_files:
        for bigram in bigrams_dict.keys():
            q = count_current_bigram(bigram, file)/count_all_bigrams(file) if count_current_bigram(bigram, file)/count_all_bigrams(file) else 1/count_all_bigrams(file)/1000
            p = math.log10(q)
            bigrams_dict[bigram] += p

    for bigram in bigrams_dict.keys():
        bigrams_dict[bigram] /= len(test_files)

    file = open('bigrams.txt', 'w')
    for bigram in bigrams_dict.keys():
        file.write(str(int.from_bytes(bigram, 'big')) + '   ' + str(bigrams_dict[bigram]) + '\n')
