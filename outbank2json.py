#!/usr/bin/env python3
import sys
import os.path
import csv
import json


def read_outbank_csv(filename_outbank_csv=None):
    """Read csv generated by Outbank V.2.22.0 Mac
    :type filename_outbank_csv: str
    """
    return_json = []
    if not filename_outbank_csv:
        raise ValueError("No Filename is passed to read_outbank_csv function")
    with open(filename_outbank_csv, 'r', encoding='UTF-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=";", quotechar='"', )
        headers = next(csv_reader)
        for csv_line in csv_reader:
            single_return_line = {}
            for index, header in enumerate(headers):
                if 'Tags' in header:
                    single_return_line[header] = csv_line[index].split()
                else:
                    single_return_line[header] = csv_line[index]
            return_json.append(single_return_line)
    return return_json


if __name__ == '__main__':
    # filename = sys.argv[1]
    filename = "./sample.csv"
    if not os.path.isfile(filename):
        raise ValueError("File dose not exists")
    print(json.dumps(read_outbank_csv(filename), sort_keys=True, indent=4))
