import socket

def parseRequest(request):
  output = {}
  r = request.decode("utf-8").split("\r\n")
  parts = r[0].split(' ')
  output["method"] = parts[0]
  output["path"] = parts[1]
  output["protocol"] = parts[2]
  output["headers"] = { (kv.split(':')[0]): kv.split(':')[1].strip() for kv in r[1:] if (len(kv.split(':')) > 1) }
  return output

s = socket.socket()
s.bind(('0.0.0.0', 8080))
s.listen(1)

while True:    
  conn, addr = s.accept()
  with conn:
    req = conn.recv(1024)
    print(req)
    r = parseRequest(req)
    path = r["path"][1:]
    if (path == ""): 
      path = "index"
    with open(f'/home/kali/Desktop/honey/modified403.html', 'rb') as file:
      html = file.read()
      conn.send('HTTP/1.1 200 OK\nContent-Type: text/html\n\n'.encode())
      conn.sendall(html)