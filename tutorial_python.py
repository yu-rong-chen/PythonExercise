'''
Create a class for linked list node
Create a class for linked list head, traverse linked list, insert node and remove node
'''

# class Node:
#     def __init__(self,dataval=None):
#         self.dataval=dataval
#         self.nextval=None
# class SLinkList:
#     def __init__(self):
#         self.head=None
#     def listprint(self):
#         pointer=self.head
#         while pointer is not None:
#             print('link:%s'% pointer.dataval)
#             pointer=pointer.nextval
#     def Atbegin(self,newdata):
#         pointer=Node(newdata)
#         pointer.nextval=self.head
#         self.head=pointer
#     def lastlist(self,newdata):
#         if self.head is None:
#             self.head=Node(newdata)
#             return
#         pointer=self.head
#         while pointer.nextval :
#             pointer=pointer.nextval
#         pointer.nextval=Node(newdata)
#     def Removenode(self,removedata):
#         HEAD = self.head
#         if HEAD is not None:
#             if HEAD.nextval == removedata:
#                 self.head=HEAD.nextval
#                 HEAD = None
#                 return
#         while HEAD is not None:
#             if HEAD.dataval == removedata:
#                 break
#             pre = HEAD
#             HEAD=HEAD.nextval
#         pre.nextval = HEAD.nextval
#         HEAD=None

# link=SLinkList()
# link.head=Node('Mon')
# link.head.nextval=Node('Tue')
# link.head.nextval.nextval=Node('Wed')
# link.listprint()
# link.Atbegin('Thurs')
# print('\n\n')
# link.lastlist('Fri')
# link.Removenode('Wed')
# link.listprint()

'''
Binary tree
Create Root, insert node, traverse the tree
If the new node is less than self.data, put it in left and vice versa.
'''
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
#     def insert(self,data):
#         if self.data:
#             if self.data > data:
#                 if self.left is None:
#                     self.left=Node(data)
#                 else:
#                     self.left.insert(data)
#             elif self.data < data:
#                 if self.right is None:
#                     self.right=Node(data)
#                 else:
#                     self.right.insert(data)
#         else:
#             self.data=Node(data)
#     def PrintTree(self):
#         if self.left:
#             self.left.PrintTree()
#         print(self.data)
#         if self.right:
#             self.right.PrintTree()
    
# root=Node(12)
# root.left=Node(6)
# root.right=Node(6)

# root.left.right=Node(8)
# root.right.left=Node(8)
# root.left.right.left=Node(7)
# root.right.left.right=Node(7)
# root.insert(6)
# root.insert(8)
# root.insert(15)
# root.insert(16)
# root.insert(9)
# root.insert(7)
# root.insert(14)
# root.PrintTree()
# import sys
# print(sys.getrecursionlimit()) # the limit of call stack

'''
Create a class for queue, add top on it and remove
Queue is first-in-first-out method

dequeue: the input and output are not restricted to a single end
'''
class Queue:
    def __init__(self):
        self.queue=list()
    def addtop(self, newdata):
        if newdata not in self.queue:
            self.queue.insert(0,newdata)
            return True
        return False
    def size(self):
        return(len(self.queue))
    def printqueue(self):
        while int(self.size()) > 0:
            print(self.queue.pop())
# Ans=Queue()
# Ans.addtop('Mon')
# Ans.addtop('Tue')
# Ans.addtop('Wed')
# Ans.addtop('TUe')
# Ans.size()
# Ans.printqueue()

# import collections
# Queue=collections.deque(['Mon','Tue','Wed','Thur'])
# Queue.append('Fri')
# Queue.appendleft('Sat')
# Queue=collections.deque([(root.left,root.right)])

# while Queue:
#     A,B=Queue.pop()
    
#     if not A and not B: continue
#     if A and B and A.data==B.data: 
#         print(A.data,B.data)
#         Queue.append((A.left,B.right))
#         Queue.append((A.right,B.left))
#     else: 
#         print('Error')

#------------------Stack-------------
# class Stack:
#     def __init__(self):
#         self.stack=[]
#     def addtop(self, newdata):
#         # use list append method to add element
#         if newdata not in self.stack:
#             self.stack.append(newdata)
#             return True
#         return False
#     def remove(self):
#         if len(self.stack) <=0:
#             return('No element in stack')
#         else:
#             self.stack.pop()
# AtStack=Stack()
# AtStack.addtop('Mon')
# AtStack.addtop('Tue')
# AtStack.addtop('Wed')
# AtStack.remove()
# print(AtStack.stack)

#--------------List Comprehension
# letter = []
# for i in 'human':
#     letter.append(i)
# letter = [i for i in 'human'] # list contains the items of the iterable string
# print(letter)


#----------------tree traversal-------

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None
#     #------insert data (binary tree)--------
#     def insert(self,data):
#         if self.data:
#             if data < self.data:
#                 if self.left is None:
#                     self.left = Node(data)
#                 else:
#                     self.left.insert(data)
#             elif data > self.data:
#                 if self.right is None:
#                     self.right = Node(data)
#                 else:
#                     self.right.insert(data)
#         else:
#             self.data=data
    
#     def PrintTree(self):
#         if self.left:
#             self.left.PrintTree()
#         print(self.data,end=' ')
#         if self.right:
#             self.right.PrintTree()
#     def inorderTraversal(self,root):
#         #----root -> left -> right
#         #Recusive solution is trival, try iterative
#         # res =[]
#         # if root:
#         #    res = self.inorderTraversal(root.left) 
#         #    res.append(root.data)
#         #    res = res+ self.inorderTraversal(root.right)
#         # return res
#         res = []
#         if root and root.left == None and root.right == None: return root.data
#         res, stack=[],[] 
#         point=root
#         while point or stack:
#             while point:
#                 stack.append(point)
#                 point=point.left
#             point=stack.pop()
#             res.append(point.data)
#             point=point.right
        
#         return res


# root=Node(21)
# root.insert(13)
# root.insert(18)
# root.insert(26)
# root.insert(24)
# root.insert(23)
# root.insert(11)
# root.insert(9)
# root.PrintTree()
# print('')
# print(root.inorderTraversal(root))