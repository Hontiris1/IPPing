#Handles adding new IP/Domain to IPlist txt file
#IP = print(newip())
#conts = print(contentsf())

def newip():
    IP = input("Add new IP: ")
    NIPopen = open("/Users/Hontiris/IPlist.txt")
    with open('IPlist.txt', mode='a') as add:
        add.write(IP)
        NIPopen.seek(0)

#Contents will read the lines on IPlist txt file
def contentsf(o):
    o = LOfIP
    LOfIP = open("/Users/Hontiris/IPlist.txt")
    with open("/Users/Hontiris/IPlist.txt", mode='r') as IPopen:
        contents = IPopen.readlines()
        LOfIP.seek(0)
