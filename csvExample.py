__author__ = 'Jorge.GarciaXimenez'
import csv
import numpy as np
import pandas as pd


df.to_csv("test.csv", sep=",")
df1 = pd.read_csv("test.csv", sep=",")
df.to_excel("test.xlsx")
data = pd.read_excel("test.xlsx", sheetname="Sheet1", index_col=None, na_values=["NA"])

print(data)
def write_csv_from_matrix(filepath,matrix):
    with open (filepath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile,delimiter=';', quotechar='"')
        csvwriter.writerow(matrix)

def write_csv_from_dataFrame(filepath,df):
    df.to_csv(filepath, sep=",")


def print_csv(filepath):
    with open (filepath, 'r', newline='') as csvfile:
        csvreader = csv.reader (csvfile,delimiter=';', quotechar='"')
        for row in csvreader:
            print (','.join(row))


def read_csv_to_dataFrame(filepath):
    df1 = pd.read_csv(filepath, sep=",")
    return df1
  #hellob hfthcgyj

