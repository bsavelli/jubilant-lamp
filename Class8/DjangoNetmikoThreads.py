#!/usr/bin/env python

from netmiko import ConnectHandler
from datetime import datetime

from net_system.models import NetworkDevice, Credentials
import django

import threading
import time


def show_arp(a_device):
	creds = a_device.credentials
	remote_conn = ConnectHandler(device_type=a_device.device_type, ip=a_device.ip_address, username=creds.username, password=creds.password, port=a_device.port, secret='')

		print a_device
		device_type = a_device.device_type
		port = a_device.port
		secret = ''
		ip = a_device.ip_address
		creds = a_device.credentials
		username = creds.username
		password = creds.password
		
		print device_type, port, ip, username, password

		print
		print '#' * 50
		print remote_conn.send_command("show arp")
		print '#' * 50
		print

	elapsed_time = datetime.now() - start_time
	print "Elapsed time: {}".format(elapsed_time)





def main():
	django.setup()

	start_time = datetime.now()
	devices = NetworkDevice.objects.all()

	for a_device in devices:
		my_thread = threading.Thread(target=show_arp, args=(a_device,))
		my_thread.start()

	main_thread = threading.currentThread()
	for some_thread in threading.enumerate():
		if some_thread != main_thread:
			print some_thread
			some_thread.join()

	print "\nElapsed time: " + str(datetime.now() - start_time)



if __name__ == "__main__":
	main()
