
import datetime
import camelcase

print(datetime.datetime.now())

print(datetime.datetime(2022,12,28))

x= datetime.datetime(2019,11,2)

print(x.strftime('%x'))

ca = camelcase.CamelCase()

text = 'hello laxman, hope you are fine'

print(ca.hump(text))

# print(dir(dict))



