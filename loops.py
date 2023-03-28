# WHILE LOOP
# number = 10

# while (number <= 10):
#    print(number)
#   number += 1

# a = 1
# while a == 1:
#   print ("Welcome to the most great year!!")
#    age = int(input("How old are you? "))

#   if age >= 22:
#       print("please come in...")
#    elif age >= 18:
#        print("you need to be over 21! get out!!")

#    else:
#        print("you are still a kid!, get out!")

# FOR LOOP
# for num in range(0, 10):
#    print(num)

# for letter in "python":
#    print ("current letter" + letter)

# NESTED LOOP
lines = int(input("How many lines ?"))
row = 0
while (row < lines):
    col = 0
    while(col < lines):
        print ("*", end='')
        col += 1
    row += 1
    print()

