import os

input = input("Enter the ip address to send the ping to >>> ")
blacklist = [" ", "&", "!", "@", "%", "^", "~", "`", "<", ">", ",", "\\", "/"]
for i in blacklist:
    if i in input:
        print("Who told you..?")
        exit()
blacklist = ["ls", "cat", "less", "tail",
             "more", "whoami", "pwd", "busybox", "echo"]
for i in blacklist:
    if i in input:
        print("Who told you..?")
        exit()

os.system("ping -c 1 " + input)
print()
