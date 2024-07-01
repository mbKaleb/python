try:
    a = 20
    b = 40
    c = 0
    print (a/c)
except ZeroDivisionError:
    print ("Zero division detected")
finally:
    print ("Code is executed by default")
