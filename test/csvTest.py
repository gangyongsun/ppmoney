# coding:utf-8
import csv

f = csv.reader(open('../csv/自助投20180828-1.csv', 'r', encoding='uTF-8'))
for i in f:
    print(i[0])
