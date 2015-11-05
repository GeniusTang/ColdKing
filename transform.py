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
	return [0, 0]
    return [parse_calender(calender) + parse_time(time), name]	
	
f = open(outputname, 'wt')

for line in lines:
    time, name = parse_line(line)
    if name:
        f.write('%-10s%s\n'%(time, name))

f.close()	



