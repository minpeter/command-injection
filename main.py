import os

input = input("Enter the ip address to send the ping to >>> ")

blacklist = [" ", "&", "!", "@", "%", "^", "~", "`", "<", ">", ",", "\\", "/"]
if any(i in blacklist for i in input):
    print("Who told you..?")
    exit()

blacklist = ["ls", "cat", "less", "tail",
             "more", "whoami", "pwd", "busybox", "echo"]
if any(i in input for i in blacklist):
    print("Who told you..?")
    exit()

os.system("ping -c 1 " + input)
print()
