import os

input = input("Enter the ip address to send the ping to >>> ")

if any(i in input for i in ["ls", "cat", "less", "tail", "more",
                            "whoami", "pwd", "busybox", "echo",
                            " ", "&", "!", "@", "%", "^", "~", "`",
                            "<", ">", ",", "\\", "/"]):
    print("Who told you..?")
    exit()

os.system("ping -c 1 " + input)
print()
