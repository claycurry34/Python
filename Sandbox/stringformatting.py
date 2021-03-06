myint = 7
mystring = "Hello"
myfloat = 6.0

print("Integer: %d" % myint)
print("String: %.2s" % mystring)
# %s string
# %

print("The integer is %d. The string is %s. The fload is %f." % (myint, mystring, myfloat))

output = "The integer is %d. The string is %s. The fload is %f."

print(output % (myint, mystring, myfloat))
