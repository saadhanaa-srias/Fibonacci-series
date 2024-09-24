def fib(n):
  if n ==0:
    return 0
  elif n==1:
    return 1
  else:
    return (fib(n-2) + (n-1))

n=int(input("enter any value to see it's fibonacci series"))
print("Fibonacci Series:",end = ' ')
for n in range(0,n):
  print(fib(n),end = ' ')
print("\n")