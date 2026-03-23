from socket  import *
from constCS import * #-

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))  #-
s.listen(1)           #-
(conn, addr) = s.accept()  # returns new socket and addr. client
while True:                # forever
  data = conn.recv(1024)   # receive data from client
  if not data: break	   # stop if client stopped
  msg = bytes.decode(data)
  tpl = eval(msg)
  n1 = tpl[0]
  n2 = tpl[1]
  op = tpl[2]

  res = 0 # guardar resultado

  if op == 'a':
    res = n1+n2
  elif op == 'm':
    res = n1 * n2
  elif op == 'd':
    res = n1 / n2
  elif op == s:
    res = n1-n2

  conn.send(str.encode(str(res))) # return sent data plus an "*"
conn.close()               # close the connection
