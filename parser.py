import re
from collections import Counter
import csv

def reader(filename):
    regemail_from = r'(from=<[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.>]+)'
    regemail_to = r'(to=<[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.>]+)'
    reg_status = r'status=\w{1,20}'
    with open(filename) as f:
        log = f.read()
        email_to = re.findall(regemail_from, log)
        email_from = re.findall(regemail_to, log)
        status = re.findall(reg_status, log)
        lists = email_from + email_to + status
        return lists

def counter(lists):
    count = Counter(lists)
    return count


def write_csv(count):
    with open('outputs.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        header = ['keys', 'value']
        writer.writerow(header)
        for item in count:
           parser = writer.writerow((item, count[item]))
        return parser

write_csv(counter(reader('maillog')))


