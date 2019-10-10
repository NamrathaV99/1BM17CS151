f1 = open("/home/bmsce/Desktop/1BM17CS151/PYTHON/primenumbers.txt", "r")
f2 = open("/home/bmsce/Desktop/1BM17CS151/PYTHON/happynumbers.txt", "r")
f2_list = f2.read()
f1_list=f1.read()
l1=f1_list.split(',')
l2=f2_list.split(',')
for i in l1:
    for j in l2:
        if(i==j):
            print(i)

f1.close()
f2.close()
