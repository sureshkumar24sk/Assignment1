n=int(input("Enter a number:"))
odd=0
even=0
for i in range(1,n+1):
    if i%2==0:
        even+=1
    else:
        odd+=1
print("The Even numbers count is",even)
print("The Odd numbers count is",odd)

       

       