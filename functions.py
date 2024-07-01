fruits = ["Apple", "Mango", "Peach"]

#Basic function
def function():
    print("output")

#Basic for loop
def loop():
    for x in range(1,6):
        print (x)
        print ("Kaleb")
# loop()

#Print Elements of a list
def listFruits():
    for fruit in fruits:
        print (fruit)
# listFruits()

#Print even numbers

# for x in range(0,21,2):
    # print (x)

def add1(a,b):
    print (a+b)
# add(1,2)

def add2(a,b):
    c = a+b
    return c

def add3(a,b):
    return a+b

def square(c):
    return c*c

print (square(add3(4,2)))


