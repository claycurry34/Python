import sys
ct = len(sys.argv)
print("Number of arguments = " + str(ct))

for n in range(0, ct):
    print("arg[" + str(n) + "] = " + str(sys.argv[n]))