import subprocess

list = subprocess.getoutput('ip n')
list = list.split('\n')

for i in range(0, (len(list))):
	item = list[i].split(' ')
	ip = item[0]
	mac = item[4]
	list[i] = [ip, mac]

list.pop(len(list)-1)

for i in range(0, len(list)):
	if(list[i][0].split('.')[3] == "1"):
		continue

	print("CONNECTED DEVICE >>      IP: ", list[i][0],"        MAC: ", list[i][1])

print("\nThere are ",len(list) - 1," devices connected at this moment.")
