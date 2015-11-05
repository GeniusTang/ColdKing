#!/usr/bin/python

fname = "Emit_revise.txt"
outputname = "Emit.txt"

MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

f = open(fname)
lines = f.readlines()
f.close()

def parse_calender(calender):
    year, month, day = map(int, calender.split('-'))
    return ((year - 2014)*365 + sum(MONTH[:month]) + day) * 24 * 60

def parse_time(time):
    hour, minute, second = map(int, time.split(':'))
    return (hour * 60 + minute)

def parse_line(line):
    try:
        calender, time, name = line.split()
    except:
	return [0, 0, 0, 0, 0, 0, 0]
    return calender.split('-') + time.split(':')[:-1] + [name] 
	
f = open(outputname, 'wt')
header = ('year', 'month', 'day', 'hour', 'minute', 'name')

for colname in header:
    f.write('%-10s'%colname)
f.write('\n')

for line in lines:
    row = parse_line(line)
    if row[0]:
        for col in row:
            f.write('%-10s'%col)
	f.write('\n')

f.close()	



