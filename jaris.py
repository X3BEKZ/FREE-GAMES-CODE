#calculate area and perimeter of a rectangle
length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))
area = length * breadth
perimeter = 2 * (length + breadth)
print("Area =", area)
print("Perimeter =", perimeter)

#determine the largest of three numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a > b and a > c:
    print("Largest number is:", a)
if b > a and b > c:
    print("Largest number is:", b)
if c > b and c > a:
    print("Largest number is:", c)

#how to find palindrome number

num = int(input("Enter a number: "))
temp = num
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
if temp == rev:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")


#LAB WORK: CHAPTER 8
# Q#1 2+4+6+... Nth 

N = int(input("Enter your Nth Term Number"))
i = 1
Sum = 0

print()
while i <= (N + 1):
    M = i * 2
    print(M, end=" ")
    i += 1
    Sum += M

print("... Nth Term")
print()
print("Sum = ", Sum)


#Q#2 10,20,30,..Nth term

p = int(input("Enter your Nth Term Number"))
i = 1
Sum = 0

print()
while i < (p + 1):
    q = i * 10
    print(q, end=",")
    i += 1
    Sum += q

print("... Nth Term")
print()
print("Sum ", Sum)

#Q#3 𝑋1+𝑋2+𝑋3+𝑋4+⋯Nth term

t = int(input("Enter your Nth Term Number"))
i = 1
Sum = 0

print()
while i <= (t + 1):
    s = t ** i
    print(t ** i, end="+")
    i += 1
    Sum += s

print("... Nth Term")
print()
print("Sum ", Sum)

#Q#4 1!+2!+3!+...Nth term

t = int(input("Enter your Nth Term Number"))
f = 1
Sum = 0
c = 1

print()
for i in range(1, t + 1):
    print(i, end="! + ")
print("... Nth Term")

print()
while c < (t + 1):
    f *= c
    print(f, end=" + ")
    c += 1
    Sum += f

print("... Nth Term")
print()
print("Sum ", Sum)

# Write a program to calculate and print the sum of even and odd integers of the first N natural numbers

n = int(input("Enter N: "))
even_sum = 0
odd_sum = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)

#Find Perfect Number

num = int(input("Enter a number: "))
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum += i
if sum == num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")

# find Grade

eng=int(input("Enter English Marks: "))
math=int(input("Enter Math Marks: "))
sci=int(input("Enter Science Marks: "))
comp=int(input("Enter Computer Marks: "))
urdu=int(input("Enter Urdu Marks: "))
per=(eng + math + sci + comp + urdu) / 5
if per >= 90:
    print("Grade A")
elif per >= 80:
    print("Grade B")
elif per >= 70:
    print("Grade C")
elif per >= 60:
    print("Grade D")
elif per >= 50:
    print("Grade E")
else:
    print("Grade F")