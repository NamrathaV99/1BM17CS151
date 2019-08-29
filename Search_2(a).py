from bisect import bisect_left
def search():
        order_list=[]
        n=int(input("Enter the no. of elements in the list : "))
        for i in range(n):
            x=int(input())
            order_list.append(x)
        key=int(input("Enter the no. to be searched : "))
        j=bisect_left(order_list,key)
        if j!=len(order_list) and order_list[j]==key:
                return True
        else:
                return False

res=search()
print(res)
        
