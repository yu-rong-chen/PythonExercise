#Leet code Num.1
# def sum(nums,target):
#     diction={}
#     for i in range(len(nums)):
#         if target-nums[i] in diction:
#             return(diction.get(target-nums[i]),i)
#         else:
#             diction[nums[i]]=i
# nums=[3,7,8,11,2]
# target =9
# index=sum(nums,target)
# print(index)

# Leet code Num.242 only the order is different (Record the number of occurrences)
# def IsAnagram(s,t):
#     dictions={};dictiont={}
#     for i in range(len(s)):
#         dictions.setdefault(s[i],0)
#         dictions[s[i]] = dictions[s[i]] +1 
#         dictiont.setdefault(t[i],0)
#         dictiont[t[i]] = dictiont[t[i]] +1 
#     if dictions==dictiont:
#         return True
#     else:
#         return False
# def IsAnagram(s,t):
    # dictions={}
    # if len(s) != len(t): return False
    # for i in s:
    #     dictions[i]=dictions.get(i,0)+1
    # print(dictions)
    # for i in t:
    #     if i not in dictions or dictions[i]<0: return False
    #     dictions[i]=dictions[i]-1
    #     # if dictions[i]<0: return False
    # return True

    # Option 2
#     from collections import Counter
#     print(Counter(s))
#     return Counter(s)==Counter(t)
# s = "gramana"
# t = "nagaram"
# print(IsAnagram(s,t))

#-------------------------Leetcode 53
# def searchInsert(listNUM,target):
#     Lmin, Lmax = 0, len(listNUM)-1
#     while Lmin <= Lmax:
#         Lmiddle = (Lmin+Lmax)//2
#         print('Lmin: %s, Lmax: %s and Lmiidle is %s'% (str(Lmin),str(Lmax),str(Lmiddle)))
#         if listNUM[Lmiddle] == target:
#             return Lmiddle
#         elif listNUM[Lmiddle] < target:
#             Lmin = Lmiddle+1
#         else:
#             Lmax = Lmiddle-1
#     print('Reuslt:Lmin: %s, Lmax: %s and Lmiidle is %s'% (str(Lmin),str(Lmax),str(Lmiddle)))
#     return Lmin
# listNUM=[1,3,5,9,11,13,14,17,20,21,25,27,29,31,33]
# target=24
# print(str(searchInsert(listNUM,target)))

#-----------------Leetcode 278 bad version
# def firstBadVersion(NUM,target):
#     Lmin, Lmax = 1, NUM
#     while Lmin <=Lmax:
#         Lmiddle = (Lmin+Lmax)//2
#         if Lmiddle >= target:
#             if target== 1:
#                 return Lmin
#             elif Lmiddle-1 == target or Lmiddle == target:
#                 return Lmiddle
#             else:
#                 Lmax=Lmiddle-1
#             print('Lmin: %s, Lmax: %s, Lmiddle:%s'% (Lmin,Lmax,Lmiddle))
#         else:
#             Lmin = Lmiddle +1

# NUM=7
# target=4
# print(firstBadVersion(NUM,target))

#-------------------Leetcode #83
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class linkedlist:
#     def __init__(self):
#         self.headval = None
#     # Function to add newnode
#     def AtEnd(self, newdata):
#         NewNode = ListNode(newdata)
#         if self.headval is None:
#             self.headval = NewNode
#             return
#         laste = self.headval
#         while(laste.next):
#             laste = laste.next
#         laste.next=NewNode
#     # Print the linked list 
#     def listprint(self):
#         printval = self.headval
#         while printval is not None:
#             print (str(printval.val)+',',end='')
#             printval = printval.next
#         print('')
# class Solution:
#     def deleteDuplicates(self):
#         ite=self.headval
#         while ite:
#             tmp=ite
#             while tmp and tmp.val == ite.val:
#                 tmp=tmp.next
#             ite.next=tmp
#             ite=ite.next
#         return self


# head = [1,1,2,3,3,4,5,5,5,5,5,5,6,6,6,6,6]
# HEAD=linkedlist()
# for i in range (0,len(head)):
#     HEAD.AtEnd(head[i])
# HEAD.listprint()
# Answer=Solution.deleteDuplicates(HEAD)
# Answer.listprint()


#-------------------Leetcode #101
# class node:
#     def __init__(self,newdata):
#         self.data=newdata
#         self.left=None
#         self.right=None

#     def isSymmtric(self):
#         from collections import deque
#         root = self
#         if root is None: return True
#         # if root.left is None and root.right is None: return True
#         # if root.left is None or root.right is None: return False
#         queue1 = deque([(root.left,root.right)])
#         while queue1:
#             l,R = queue1.pop()
#             if l is None and R is None: continue
#             if l is None or R is None: return False
#             if l.data != R.data: return False
#             queue1.append((l.left,R.right))
#             queue1.append((l.right,R.left))
#             print(l.data,R.data)
#         return True

# test=node(12)
# test.left=node(6)
# test.right=node(6)
# test.left.right=node(8)
# test.right.left=node(8)
# test.left.right.left=node(7)
# test.right.left.right=node(7)
# test.left.right.right=node(9)
# test.right.left.left=node(9)

# Ans=test.isSymmtric()
# print(Ans)

#------------Leetcode 617
# class Tree:
#     def __init__(self,newdata):
#         self.data=newdata
#         self.left = None
#         self.right = None
#     def printNode(self):
#         if self.left:
#             self.left.printNode()
#         print(self.data)
#         if self.right:
#             self.right.printNode()

# def summary(Node1,Node2):
#     #----------solution 1 - recursive-----
#     # if not Node1 and not Node2: return None
#     # if not Node1 or not Node2: return Node1 or Node2
#     # Node1.data += Node2.data
#     # summary(Node1.left,Node2.left)
#     # summary(Node1.right,Node2.right)
#     # return Node1
#     #---------solution 2 - iterative
#     stack=[]
#     stack.append((Node1,Node2))
#     while stack:
#         l,r = stack.pop()
#         if not r or r.data=='NULL': continue
        # l.data+=r.data

#         if not l.right:
#             l.right = r.right
#         else:
#             stack.append((l.right,r.right))
#         if not l.left:
#             l.left = r.left
#         else:
#             stack.append((l.left,r.left))
#     return Node1

# Node1 = Tree(1)
# Node1.left = Tree(2)
# Node1.right = Tree(3)
# Node1.left.left = Tree(4)
# # Node1.right.right = Tree(8)

# Node2 = Tree(10)
# Node2.left = Tree(9)
# Node2.right = Tree(8)
# Node2.left.left = Tree('NULL')
# Node2.left.right = Tree(7)
# Node2.right.right = Tree(5)
# Node3 = summary(Node1,Node2)
# Node2.printNode()
# print('Node1')
# Node3.printNode()

#----------------Leetcode 62
# letter=[]
# for i in 'humans':
#     letter.append(i)
# print(letter)

# matrix = [[0 for x in range(4)] for y in range(3)]
# for i in range(4):
#     for j in range(3):
#         if i==0 or j==0:
#             matrix[j][i] =1
#         else:
#             matrix[j][i]=matrix[j][i-1]+matrix[j-1][i]

# print(matrix)

#----------------Leetcode 63
A= [[0,0,0],[0,1,0],[0,0,0],[1,1,0]]
# A = [[0,0]]
# matrix =A
# m = len(A)
# n = len(A[0])
# for i in range(n):
#     for j in range(m):
#         if i ==0 or j==0:
#             if matrix[j][i] ==1:
#                 matrix[j][i] =0
#             else:
#                 matrix[j][i] = 1
#         else:
#             if matrix[j][i] ==1:
#                 matrix[j][i] =0
#             else:
#                 matrix[j][i] = matrix[j-1][i]+matrix[j][i-1]

# print(matrix)
#-----------------Answer-----------------
# if not A or A[0][0]==1:
#     print('0')
# m,n=len(A),len(A[0])
# dp =[[0 for x in range(n)] for y in range(m)]
# dp[0][0]=1
# for i in range(m):
#     for j in range(n):
#         if A[i][j]==0:
#             if i-1>=0:
#                 dp[i][j]+=dp[i-1][j]
#             if j-1>=0:
#                 dp[i][j]+=dp[i][j-1]
# print(A)
# print(dp)

#--------------------Leetocode 198
# Nums = [2,1,1,2]
# rob = [0 for x in range(len(Nums))]
# print(rob)
# rob[0] = Nums[0]
# rob[1]= max(Nums[0], Nums[1])
# for i in range (2,len(Nums)):
#     rob[i]=max(Nums[i]+rob[i-2],rob[i-1])
# print(rob)

#---------------------Leetoce 213
# nums=[100,3,1,3]
# # if not nums: return 0
# # if len(nums) == 1: return nums[0]
# # if len(nums) == 2: return max(nums[0],nums[1])
# index=[0 for x in range(len(nums))]
# L = len(nums)
# index[0] = nums[0]
# index[1] = max(index[0],nums[1])

# for i in range (2, L):
#     if i==L-1:
#         if L%2 == 0:
#             index[i] = max(nums[i]+index[i-2],index[i-1])
#         else:
#             index[i] = max(nums[i]+index[i-2]-index[0],index[i-1])
#     else:
#         index[i] = max(nums[i]+index[i-2],index[i-1])
# print(index)

#-----------------Leetcode 94 - binary tree inorder transversal
#-----------------Leetcode 102 - Binary Tree Order Traversal
class Node:
    def __init__(self,data):
        self.val=data
        self.left=None 
        self.right=None 
        self.last=None
    def insertdata(self,data):
        if self.val:
            if data < self.val:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insertdata(data)
            if data > self.val:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insertdata(data)
        else:
            self.val=data
    def printTree(self):
        pointer = self
        if pointer.left:
            pointer.left.printTree()
        print(pointer.val,end=' ')
        if pointer.right:
            pointer.right.printTree()

    def inorderTraversal(self,root):
        #-------------iterative ---
        # res,curr=[],[]
        # pointer=root
        # while curr or pointer:
        #     while pointer:
        #         curr.append(pointer)
        #         pointer = pointer.left
        #     pointer = curr.pop()
        #     res.append(pointer.val)
        #     pointer = pointer.right
        # return res
        #--------------recursive ---
        res= []
        def dfs(root):
            if root.left: dfs(root.left)
            res.append(root.val)
            if root.right: dfs(root.right)
        dfs(root)
        return res
    def levelOrder(self,root):
        # #----------------recursive ----
        # res=[]
        # if res is None: return res
        # res.append([]) # Create 2 dimenson list to save the depth and node
        # def helper(n,res,level):
        #     if not n: return
        #     if len(res)-1 < level:  # if res didn't have the list for specific depth, then append directly
        #         res.append([n.val])
        #     else: # if res already have the list of specific depth, then append it on specific list
        #         res[level].append(n.val)
        #     helper(n.left,res,level+1) # level 1 -> to save root.left and root.right
        #     helper(n.right,res,level+1)
        # helper(root,res,0) # level 0 -> len(res) is 1 to save root
        # return res

        #----------------iterative ----
        from collections import deque #--------a generalzation of stack and queues
        res=[]
        if not root: return res
        q=deque([root]) #------Node Object is not iteratable, put root in []
        while q:
            cnt = len(q) # check how many Node at one level
            level =[]
            for _ in range(cnt):
                n=q.popleft()
                level.append(n.val)
                if n.left: q.append(n.left)
                if n.right: q.append(n.right)
            res.append(level)
        return res
    #----------------700 Search in Binary Search Tree---
    def BST(self,root,val):
        #----------iterative-------
        pointer=root
        while pointer:
            if pointer.val > val:
                pointer = pointer.left
            elif pointer.val < val:
                pointer = pointer.right
            elif pointer.val == val:
                return pointer
        return None
        #------------recursive----------
        # if not root or root.val == val:
        #     return root
        # if root.val > val:
        #     return self.BST(root.left,val)
        # else:
        #     return self.BST(root.right,val)

    #-------------Leetcode 98 Validate Binary Search Tree----
    def ValidateBST(self,root):
        #-----iterative
        # if not root: return True
        # pre, curr, pointer=None,[],root
        # while curr or pointer:
        #     while pointer:
        #         curr.append(pointer)
        #         pointer=pointer.left
        #     pointer=curr.pop()
        #     if pre and pointer.val <= pre.val:
        #         return False
        #     pre = pointer
        #     pointer=pointer.right
        # return True 

    #------recursive----
        if not root: return True
        if not self.ValidateBST(root.left): return False
        if self.last and self.last.val >= root.val: return False
        self.last=root
        return self.ValidateBST(root.right)

    
# Head = Node(14)
# Head.insertdata(9)
# Head.insertdata(8)
# Head.insertdata(12)
# Head.insertdata(13)
# Head.insertdata(18)
# Head.insertdata(16)
# Head.insertdata(19)
# Head.printTree()
# print(' ')
# print(Head.inorderTraversal(Head))
# print(Head.levelOrder(Head))
# print(Head.BST(Head,9))
# print(Head.ValidateBST(Head))

# Test = Node(0)
# Test.left=None
# Test.right=Node(-1)
# print(Test.ValidateBST(Test))

#-------Leetcode 136
# nums=[4,1,2,1,2]

# res = 0
# for i in nums:
#     res ^= i # Bitwise Operation - exclusive OR: 01 and 10 will output 1, otherwise 0
#     # res = res ^ i
# print(res)

#------Leetcode 693 binary number with alternating bits
# '''
# n         =  1 0 1 0 1 0 1 0
# n>>1      =  0 1 0 1 0 1 0 1
# n>>1 ^ n  =  1 1 1 1 1 1 1 1
# m=n
# m+1       =1 0 0 0 0 0 0 0 0 
# (m+1)&m   =0 0 0 0 0 0 0 0 0

# '''
# n=5
# m=n>>1 # n binary right shift 1
# o=n^m # XOR if n and m are different, the result is 1
# Answer = o & (o+1) # If answer ==1 return True

# n = n ^ (n >> 1)
# return n & (n+1)

#----------Leetcode 67 Add Binary
A = '1010'
B = '101101'

# i,j = len(A)-1, len(B)-1
# res, c = [],'0'

# while i>=0 or j>=0 or c=='1':
#     ai = A[i] if i>=0 else '0'
#     bj = B[j] if j>=0 else '0'
#     if ai == bj:
#         res.append(c)
#         c=ai
#     else:
#         res.append('0' if c == '1' else '1')
#     i = i-1
#     j=j-1
# print(res)
# print(''.join(res[::-1]))

# Leetcode 680 valid Palindrom II
S = 'abca'
i, j = 0, len(S)-1

