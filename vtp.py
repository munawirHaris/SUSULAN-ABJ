while True:
    print("*"*20)
    print("Menu VTP")
    print("*"*20)
    print("1. Add New VTP")
    print("2. Show VTP")
    print("0. Exit")
    print("*"*20)
    y=input("Enter the choise: ")
    print("*"*20)
    if y == "1":
        while True:
            file = open ("vtp-databases.txt", "a")
            lanjut = input("Enter Device Hostname or type 0 to stop: ")
            if lanjut == "0" :
                break
            elif lanjut != "0":
                Vtp_mode = input("Enter VTP Mode [Server/Access/Transparant] : ")
            file.write("Device Hostname : " + lanjut +", \t VTP Mode : " + Vtp_mode +"\n" )
    elif y == "2" :
        file = open ("vtp-databases.txt", "r")
        print("*"*20)    
        for item in file:
            item = item.strip()
            print(item)
    elif y == "0":
        break
    elif y != "1" and "2" and "0":
        print("\n please provide valid input!\n")