#name: Cassidy Ward
#date: 10/13/2021
#description: this program

num = int(input("Please enter a positive integer: "))

print("The factors of",num,"are:")

for i in range(1, num + 1):

    if num % i == 0:

         print(i)