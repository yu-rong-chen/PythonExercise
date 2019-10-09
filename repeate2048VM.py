allguest=[]

FHead = open("C:\\Users\\chenyur\\OneDrive - Hewlett Packard Enterprise\\Spring\\modular test\\test report\\1705\\data\\Head.txt", "r")
fans = open("C:\\Users\\chenyur\\OneDrive - Hewlett Packard Enterprise\\Spring\\modular test\\test report\\1705\\data\\ans.txt", "w")
fans.write(FHead.read())
FHead.close()
fans.close()

guest_num = 10
repete_num =205 #2047/20~=103

for times in range(repete_num):
    for num in range (0,guest_num,1):
        print(num)
        A='\t{\n\t'
        B='\t\t"id": "'+str(num+times*guest_num)+'",\n'

        file="C:\\Users\\chenyur\\OneDrive - Hewlett Packard Enterprise\\Spring\\modular test\\test report\\1705\\data\\guest"+str(num)+".txt"
        f = open(file, "r")
        C=f.read()
        f.close()
        allguest=A+B+C
        
        fans = open("C:\\Users\\chenyur\\OneDrive - Hewlett Packard Enterprise\\Spring\\modular test\\test report\\1705\\data\\ans.txt", "a")
        fans.write(allguest)
        fans.close()
        
FTail = open("C:\\Users\\chenyur\\OneDrive - Hewlett Packard Enterprise\\Spring\\modular test\\test report\\1705\\data\\Tail.txt", "r")
fans = open("C:\\Users\\chenyur\\OneDrive - Hewlett Packard Enterprise\\Spring\\modular test\\test report\\1705\\data\\ans.txt", "a")
fans.write(FTail.read())
fans.close()
FTail.close()

#-------remember delete , at the end of the guest-----------------------------------
