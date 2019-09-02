allguest=[]

FHead = open("C:/Users/chenyur/OneDrive - Hewlett Packard Enterprise/Spring/1705/data/Head.txt", "r")
fans = open("C:/Users/chenyur/OneDrive - Hewlett Packard Enterprise/Spring/1705/data/ans.txt", "w")
fans.write(FHead.read())
FHead.close()
fans.close()


for times in range(205):
    for num in range (10):
        print(num)
        A='\t{\n\t'
        B='\t\t"id": "'+str(num+times*10)+'",\n'

        file="C:/Users/chenyur/OneDrive - Hewlett Packard Enterprise/Spring/1705/data/guest"+str(num)+".txt"
        f = open(file, "r")
        C=f.read()
        f.close()
        allguest=A+B+C
        
        fans = open("C:/Users/chenyur/OneDrive - Hewlett Packard Enterprise/Spring/1705/data/ans.txt", "a")
        fans.write(allguest)
        fans.close()
        
FTail = open("C:/Users/chenyur/OneDrive - Hewlett Packard Enterprise/Spring/1705/data/Tail.txt", "r")
fans = open("C:/Users/chenyur/OneDrive - Hewlett Packard Enterprise/Spring/1705/data/ans.txt", "a")
fans.write(FTail.read())
fans.close()
FTail.close()

#-------remember delete , at the end of the guest-----------------------------------
