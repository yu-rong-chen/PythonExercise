# RDIMM_Memory=['32768 MB', '32768 MB', '32768 MB', '32768 MB', '32768 MB', '32768 MB', '32768 MB', '32768 MB']
# B=list(map(int, ''.join([x if x.isdigit() else ' ' for x in str(RDIMM_Memory)]).split()))  # extract number from string
# print(B)

# for x in str(RDIMM_Memory):
#     if x.isdigit():
#         A=''.join(x)

# print(A)

## test 1
# def collatz(number):
#     try:
#         int(number)
#         while number != 1:
#             if number%2==0:
#                 print(str(number/2))
#                 number=number/2
#             elif number%2==1:
#                 print(str(number*3+1))
#                 number=number*3+1
#     except ValueError:
#         print('please input integer')

# print('please input a number')
# collatz(input())

## list
# def comma(spam):
#     for i in spam:
#         if i == spam[-1]:
#             print('and '+i)
#         else:
#             print(i+',' , end =" ")

# spam=[]
# while True:
#     print('Please input your inventory')
#     inventory = input()
#     if inventory == '':
#         break
#     spam.append(inventory)
# comma(spam)

# grid=[['.','.','.','.','.','.'],
#       ['.','0','0','.','.','.'],
#       ['0','0','0','0','.','.'],
#       ['0','0','0','0','0','.'],
#       ['.','0','0','0','0','0'],
#       ['0','0','0','0','0','.'],
#       ['0','0','0','0','.','.'],
#       ['.','0','0','.','.','.'],
#       ['.','.','.','.','.','.']]

# for j in range (6):
#     for i in range (9):
#         print(grid[i][j], end = '')
#     print('')

# #chapter dictionary
# def displayInventory(inventory):
#     print('Inventory:'.center(17,'-'))
#     item_total=0
#     for i,v in inventory.items():
#         # print(str(i) +':'+ str(inventory.get(i)))
#         print(str(i).ljust(12,'.') + str(v).rjust(5))
#         item_total=item_total+int(v)
#     print('Total number of items:'+str(item_total))
# def addInventory(inventory,addedItems):
#     for i in addedItems:
#         inventory.setdefault(i,0) #If there is no item in inventory, assign 0. If there is, remain original value
#         inventory[i]=inventory[i]+1
#     return(inventory)

# inventory = {'row':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}
# displayInventory(inventory)
# dragonLoot=['gold coin','dagger','gold coin','gold coin','ruby']
# inventory=addInventory(inventory,dragonLoot)
# displayInventory(inventory)


# def func():
#     raise IOError
# def this_fails():
#     x=1/0
# try:
#     # func()
#     this_fails()
# except IOError as exc:
#     print('Handling Error', exc)
#     print('NO exc')
#     raise RuntimeError('------------------------------------------HO----------------------------------')
#     # raise RuntimeError('-----------------------------------------Failed to open database--------------') from exc
# except ZeroDivisionError as error:
#     print('Can not divise 0')
#     print('Show error: ', error)
#     # raise RuntimeError('Error')
#     # raise RuntimeError('Error:', error)
#     raise RuntimeError('Errorrr') from error

# my_module.py

class Complex:
    def __init__(self,realpart,imagpart):
        self.r=realpart
        self.i=imagpart

x=Complex(3.0,-4.5)
x.counter=1
while x.counter<10:
    x.counter=x.counter*2
    print(x.counter)
print(x.counter)
del x.counter