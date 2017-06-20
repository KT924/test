#!/usr/bin/python3

import xlrd

def value1():
    result=[]
    fname='/var/www/html/chart/test/data.xls'
    bk=xlrd.open_workbook(fname)
    sh=bk.sheet_by_name('Sheet1')
    rows=sh.nrows
    for i in range(0,rows):
         result.append(sh.row_values(i)[0])
    return result

def value2():
    result=[]
    fname='/var/www/html/chart/test/data.xls'
    bk=xlrd.open_workbook(fname)
    sh=bk.sheet_by_name('Sheet1')
    rows=sh.nrows
    for i in range(0,rows):
         result.append(sh.row_values(i)[1])
    return result
