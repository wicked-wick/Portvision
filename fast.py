from termcolor import colored
from socket import *
from threading import *
import optparse
def fullscan(host1,j):
	try:
		sock1=socket(AF_INET,SOCK_STREAM)
		setdefaulttimeout(2)
		sock1.connect((host1,j))
		print(colored("[+]{}/tcp open".format(j),'green'))
	except:
		print(colored("[+]{}/tcp is closed".format(j),'red'))
def portscan(h1):
	try:
		nu=gethostbyname(h1)
	except:
		print("Hostname {} not resolved".format(h1))
	try:
		name=gethostbyaddr(nu)
		print('[+]Scanning for {}'.format(name))
	except:
		print('[+]Scanning for {}'.format(nu))
	for ports in range(0,1001):
		t=Thread(target=fullscan, args=(h1,ports))
		t.start()
def main():
	gop=optparse.OptionParser('Usage:' + ' -H<specify host to scan>')
	gop.add_option('-H', dest='tghost', type='string', help='Specify the Host for scanning')
	(options,args)=gop.parse_args()
	tghos=options.tghost
	if (tghos==None):
		print(gop.usage)
		exit(0)
	portscan(tghos)
	
if __name__=='__main__':
	main()
