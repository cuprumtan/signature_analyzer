import datetime
import os


def search_virus(signature, signature_file, search_dir, log_file):
    
    log = open(log_file, 'a')
    log.write(str(datetime.datetime.now()) + '| Start searching...\n')
    
    search_files = os.listdir(search_dir)
    search_files = [search_dir + '\\' + x for x in search_files]

    count = 0
    relevant_count = 1

    for search_file in search_files:
        if signature in open(search_file, 'rb').read():
            count += 1
            log.write(str(datetime.datetime.now()) + '| Found signature in ' + str(search_file) + ' ')
            if search_file.rsplit('\\', 1)[1] == signature_file.rsplit('\\', 1)[1]:
                log.write('File relevant.\n')
            else:
                log.write('File NOT relevant.\n')
            print('Signature detected! File: ' + search_file)

    accuracy = relevant_count / count * 100
    log.write(str(datetime.datetime.now()) + '| Search accuracy: ' + str(accuracy) + '%\n')

    print('Search accuracy: ' + str(accuracy) + '%')
