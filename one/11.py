__author__ = 'cc'

p = (4, 5)
x, y = p
print x
print y

data = ['ACME', 50, 91.1, (2012, 12, 31)]
name, shares, price, date = data
print name
print date

name, shares, price, (year, mon, day) = data
print year, mon, day

s = 'Hello'
a, b, c, d, e = s
print a, b, e