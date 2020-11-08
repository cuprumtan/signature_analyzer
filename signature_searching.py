import datetime
import os


# signature total probability = log10(p(bigram_1)) + log10(p(bigram_2)) + ...
def get_signature_P(signature, bigrams_dict):
    P = 0
    for index in range(0, len(signature) - 1):
        P += bigrams_dict[signature[index:index + 2]]
    return P


def get_signature(bigrams_dict, signature_file, signature_size, test_dir, log_file):

    log = open(log_file, 'a')
    log.write(str(datetime.datetime.now()) + '| Starting new session\n')
    log.write(str(datetime.datetime.now()) + '| Test files in ' + str(test_dir) + '\n')
    log.write(str(datetime.datetime.now()) + '| Signature file ' + str(signature_file) + '\n')
    log.write(str(datetime.datetime.now()) + '| Signature size ' + str(signature_size) + 'bytes\n')

    test_files = os.listdir(test_dir)
    test_files = [test_dir + '\\' + x for x in test_files]
    try:
        test_files.remove(signature_file)
    except Exception:
        log.write(str(datetime.datetime.now()) + '[WARNING] Tried to exclude signature file: no such file in test_dir\n')

    size = os.path.getsize(signature_file)
    file = open(signature_file, 'rb').read()

    etalon_signature = b'\x00'
    etalon_P = 1

    signature_flag = 0

    for signature_index in range(0, size - signature_size + 1):
        signature = file[signature_index:signature_index + signature_size]
        for test_file in test_files:
            if signature in open(test_file, 'rb').read():
                signature_flag = 1
        if signature_flag:
            # get signature with the smallest total probability
            P = get_signature_P(signature, bigrams_dict)
            if P < etalon_P:
                etalon_P = P
                etalon_signature = signature

    log.write(str(datetime.datetime.now()) + '| Etalon signature: ' + str(etalon_signature) + '\n')

    return etalon_signature
