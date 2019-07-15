import socket
import commands

s=socket.socket()
s.bind((socket.gethostname(),1034));
s.listen(5);
while True:
	c,addr=s.accept()
	print("accept:",addr)
	length=c.recv(4)
	if length==0:
		cmd_s,cmd_r=commands.getstatusoutput("ssserver -c /etc/shadowsocks.json -d stop")
	elif length==1:
		cmd_s,cmd_r=commands.getstatusoutput("ssserver -c /etc/shadowsocks.json -d start")
	c.sendall(cmd_r)
