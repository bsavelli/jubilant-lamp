#!/usr/bin/env python


import pexpect
import sys
import re
from getpass import getpass

def main():
	ip_addr = '10.0.1.1'
	username = 'admin'
	password = getpass()
	port = 22

	ssh_con = pexpect.spawn ('ssh -l {} {} -p {}'.format(username, ip_addr, port))
	#ssh_con.logfile = sys.stdout
	ssh_con.timeout = 15
	ssh_con.expect('ssword:')

	ssh_con.sendline(password)
	
	ssh_con.expect('#')
	print ssh_con.before
	ssh_con.sendline('show ip int brief')
	ssh_con.expect('#')

	ssh_con.sendline('terminal length 0')
	ssh_con.expect('#')

	ssh_con.sendline('show version')
	ssh_con.expect('3313Router#')

	print ssh_con.before
	print ssh_con.after

	pattern = re.compile(r'^Lic.*DI:.*$', re.MULTILINE)
	ssh_con.sendline('show version')
	ssh_con.expect(pattern)
	print ssh_con.after


if __name__ == "__main__":
	main()
