#################################################################
#                           Honts IPChecker                     #
#################################################################


#This will add a new IP to the IPlist
def newip():
    IP = input("Add new IP: ")

    ipopen = open("IPlist.txt")
    with open('IPlist.txt', mode='a') as add:
        add.write("\n{}".format(IP))
        ipopen.close()

#This will each line on the IPlist.txt file
def contents():
    ipopen = open("IPlist.txt")
    with open("IPlist.txt", mode='r') as read:
        read = ipopen.readlines()
        ipopen.seek(0)
        ipopen.close()
    return read


def scanlist():
    ipopen = open("IPlist.txt")

    #Opens the IPlist.txt file and strips each of the lines so that we can read individually.
    with open("IPlist.txt", "r+") as ips_file:
        ips = [ip.strip() for ip in ips_file.readlines()]

    #Read each line from the IPlist.txt file
    with open("IPlist.txt", "r") as available_ips_file:
        for ip in ips:
            #Pings each line from the IPlist.txt file
            response = os.system('ping {}'.format(ip))

            if response == 0:  # 512/DOWN value - 0/UP value
                # Up
                print("- Ip Address:", ip, 'is up!')
            elif response == 512:
                #down
                print("- IP Address:", ip, 'is down!')
            else:
                #other error
                print("- Unkown host or other error!")
