def printDivisors(n):
    i=1;
    print("Divisors : ")
    while(i<=n):
        if(n%i==0):
            print(i)
        i+=1

n=int(input("Enter the no. : "))
printDivisors(n)
