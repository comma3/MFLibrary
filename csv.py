import csv


def read_to_list(filename):
    """
    Opens the indicated filename and creates a list line by line
    """
    listoutput = []
    with open(filename) as file:
        entries = csv.reader(file)
        for item in entries:
            listoutput.append(item)
    return listoutput


def read_cto_dictionary(filename):
    """
    Opens the indicated filename and creates a list line by line using the first entry on each line
    as the key and the second as the value
    """
    dictionaryoutput = {}
    with open(filename) as file:
        entries = csv.reader(file)
        for item in entries:
            dictionaryoutput[item[0]] = item[1]
    return dictionaryoutput


def read_to_2tuple_dictionary(filename):
    """
    Opens the indicated filename and creates a list line by line using the first two entries on each line
    written as a tuple as the key and the third item as the value
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
    with open(outputfilename, 'w', newline='') as outfile:
        itemwriter = csv.writer(outfile, delimiter=",")
        for item in list:
            itemwriter.writerow(item)


def write_dict(outputfilename, dictionary):
    with open(outputfilename, 'w', newline='') as outfile:
        for key, value in dictionary.items():
            outfile.write('%s,%s\n' % (key, value))
