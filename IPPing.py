import os

IP = input("Enter IP ")

response = os.system("ping -a -c 2 " + IP) #(-a adds beep wen connection as been established, -c Stops the pinging when done, -q to view only the ping statistics summary as shown below.)

if response == 0: # 512/DOWN value - 0/UP value
    #Up
    print("- Ip Address:",IP, 'is up!')
elif response <= 512:
    print("- IP Address:",IP, 'is down!')
else:
    #Down
    print("- Unkown host or other error!")
