#python program to find factorial number


n = int(input("Enter the number : "))

factorial = 1

if n < 0:
   print ("Factorial do not exist for negative number")

elif n == 0:
   print ("Factorial 0 is 1")

else:
  for i in range(1, n + 1):
    factorial = factorial*i

  print ("Factorial of",n,"is",factorial)