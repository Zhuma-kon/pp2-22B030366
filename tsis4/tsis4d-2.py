import datetime
x=datetime.datetime.now()
c=x-datetime.timedelta(days=1)
b=x+datetime.timedelta(days=1)
print(c)
print(x)
print(b)