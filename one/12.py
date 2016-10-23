__author__ = 'cc'


def drop_first_last(grades):
    first, *middle, last = grades
    n = 0
    for i in middle:
        n += i
    return n / (len(middle) + 1.0)


print(drop_first_last([1, 2, 3, 4, 5, 6, 7]))

record = ('Dave', 'dave@example.com', '777-555-1212', '847-555-1212')

name, email, *phone_number = record
print(phone_number)

file = open('/etc/passwd')
lines = file.readlines()
for line in lines:
    uname, *fields, homedir, sh = line.split(':')
    print(uname, homedir)
