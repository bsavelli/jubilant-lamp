
import paramiko
import time


# VARIABLES THAT NEED CHANGED
ip = '10.0.1.1'
username = 'admin'
password = 'admin'

    # Create instance of SSHClient object
remote_conn_pre = paramiko.SSHClient()

    # Automatically add untrusted hosts (make sure okay for security policy in your environment)
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # initiate SSH connection
remote_conn_pre.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False)
print "SSH connection established to %s" % ip

    # Use invoke_shell to establish an 'interactive session'
remote_conn = remote_conn_pre.invoke_shell()
print "Interactive SSH session established"

    # Strip the initial router prompt
output = remote_conn.recv(1000)

    # See what we have
print output

    # Turn off paging
#disable_paging(remote_conn)

    # Now let's try to send the router a command
remote_conn.send("\n")
remote_conn.send("show ip int brief\n")

    # Wait for the command to complete
time.sleep(2)
    
output = remote_conn.recv(5000)
print output
remote_conn.send("\n")
remote_conn.send("show int description\n")

    # Wait for the command to complete
time.sleep(2)
    
output = remote_conn.recv(5000)
print output
