
def evenlist(A):
    newlist=[]
    for i in A:
        if(i % 2==0):
            newlist.append(i)
    print("Even list : ", newlist)
list1=[]
n=int(input("Enter the size of the list : "))
print("Enter the elements of the list : ")
for i in range(n):
      x=int(input( ))
      list1.append(x)
print("List : ",list1)
evenlist(list1)
