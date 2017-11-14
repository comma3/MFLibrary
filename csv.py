import csv


def read_list(filename):
    """
    Opens the indicated filename and creates a list line by line

    PARAMS: filename
    """
    listoutput = []
    with open(filename) as file:
        entries = csv.reader(file)
        for item in entries:
            listoutput.append(item)
    return listoutput


def read_dictionary(filename):
    """
    Opens the indicated filename and creates a list line by line using the first entry on each line
    as the key and the second as the value

    PARAMS: filename
    """
    dictionaryoutput = {}
    with open(filename) as file:
        entries = csv.reader(file)
        for item in entries:
            dictionaryoutput[item[0]] = item[1]
    return dictionaryoutput

def read_reverse_dictionary(filename):
    """
    Opens the indicated filename and creates a list line by line using the first entry on each line
    as the key and the second as the value

    PARAMS: filename
    """
    dictionaryoutput = {}
    with open(filename) as file:
        entries = csv.reader(file)
        for item in entries:
            dictionaryoutput[item[1]] = item[0]
    return dictionaryoutput


def read_2tuple_dictionary(filename):
    """
    Opens the indicated filename and creates a list line by line using the first two entries on each line
    written as a tuple as the key and the third item as the value

    PARAMS: filename
    """
    dictionaryoutput = {}
    with open(filename) as file:
        entries = csv.reader(file)
        for item in entries:
            # use tuple of company (i.e., VEST01, etc) and item
            # companies have different prices
            dictionaryoutput[(item[0], item[1])] = item[2]
    return dictionaryoutput


def write_list(outputfilename, list):
    """
    Writes a list to a csv.

    PARAMS: filename, list
    """
    try:
        with open(outputfilename, 'w', newline='', encoding='utf-8') as outfile:
            itemwriter = csv.writer(outfile, delimiter=",")
            for item in list:
                itemwriter.writerow(item)
    except:
        input("File still open! Please close and press enter to continue")
        with open(outputfilename, 'w', newline='', encoding='utf-8') as outfile:
            itemwriter = csv.writer(outfile, delimiter=",")
            for item in list:
                itemwriter.writerow(item)


def write_dict(outputfilename, dictionary):
    """
    Writes a dictionary to a csv.

    PARAMS: filename, dictionary
    """
    # May want to modify this code to pickle the key and value and alter the read dictionary to do the same.
    try:
        with open(outputfilename, 'w', newline='', encoding='utf-8') as outfile:
            for key, value in dictionary.items():
                outfile.write('%s,%s\n' % (key, value))
    except:
        input("File still open! Please close and press enter to continue")
        with open(outputfilename, 'w', newline='', encoding='utf-8') as outfile:
            for key, value in dictionary.items():
                outfile.write('%s,%s\n' % (key, value))
