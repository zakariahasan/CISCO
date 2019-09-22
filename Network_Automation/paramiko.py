try:
	import paramiko

except:

	pip3 install paramiko



ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoPolicy())

ssh.connect('192.168.10.3',port=22,username='zakaria',password='test321')

stdin, stdout, stderr = ssh.exec_command('copy tftp: flash')

stdin.write('192.168.10.2')
stdin.write('\n')
stdin.flush()
stdin.write('source_test.txt')
stdin.write('\n')
stdin.flush()
stdin.write('dest_test.txt')
stdin.write('\n')


output = stdout.readlines()
print ('\n'.join(output))

ssh.close()
