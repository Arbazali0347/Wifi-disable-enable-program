import os
import time
me = input("Enter Choice: ")
secods = int(input("enter your seconds: "))
# 10 minutes ke liye wait karo (10 minutes = 600 seconds)
time.sleep(secods)

# Wi-Fi Disable kar do
if me == "disable":
    os.system('netsh interface set interface "Wi-Fi" admin=disable')
elif me == "enable":
    os.system('netsh interface set interface "Wi-Fi" admin=enable')
else:
    print("Enter choice! please")
print("Wi-Fi has been disabled after 10 minutes.")