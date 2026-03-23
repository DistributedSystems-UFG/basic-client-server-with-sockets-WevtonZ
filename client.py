from socket  import *
from constCS import * #-
from datetime import datetime

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) # connect to server (block until accepted)

# a = add, s = subtract, m = multiply, d = divide

# msg = (20, 30, 'a')
# msg = (20, 30, 'm')
# msg = (45, 25, 's')
msg = (60, 13, 'd')

t1 = datetime.now()
s.send(str.encode(str(msg)))  # send some data
data = s.recv(1024)     # receive the response
t2 = datetime.now()
print(bytes.decode(data))
print (data.decode())            # print the result
print(t2-t1)
s.close()               # close the connection
