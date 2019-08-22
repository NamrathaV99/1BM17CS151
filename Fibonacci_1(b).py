def fibonacci(n):
    if(n<=1):
        return n
    else:
        return(fibonacci(n-1)+fibonacci(n-2))

n=int(input("Enter the no. of Fibonacci numbers : "))
print("Fibonacci Series : ")
fib=[]
for i in range(n):
    x=fibonacci(i)
    fib.append(x)
print(fib)
