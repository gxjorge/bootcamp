__author__ = 'Jorge.GarciaXimenez'
import csv

def write_csv():
    with open ("eggs.csv", 'w', newline='') as csvfile:
        csvwriter= csv.writer(csvfile,delimiter=';', quotechar='"')
        csvwriter.writerow(['hello', 'hello, hello'])

def read_csv():
    with open ("eggs.csv", 'r', newline='') as csvfile:
        csvreader= csv.reader (csvfile,delimiter=';', quotechar='"')
        for row in csvreader:
            print (','.join(row))

def main():
    write_csv()
    read_csv()


if __name__ == '__main__':
  main()