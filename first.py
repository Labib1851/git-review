# number print
i = 2
while i <= 100:     # Loop will continue as long as i is less than or equal to 10
    print(i)       # Print the current value of i
    i = i + 2      # Increment i by 1 in each iteration
print("end")       # After the loop ends, print "end"

# print sum
sum = 0
i = 1
while i<=51:
    sum = sum + i
    i = i + 2
print(sum)    

sum = 0
i = 1
while i<=100:
    if i % 7 != 0:
        sum = sum + i
    i = i + 1
print(sum)


# fobonacci program
n = int(input("entar the nember:"))
a, b =0, 1
print("Fibonacci :")
while a <= n:
    print(a, end=" ")
    a, b = b,a + b