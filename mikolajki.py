from random import shuffle
l = ["Wojtus","Tomus","Kacpix","Gosienka","Martusia","Irenka","Olusia","Sylwusia","Adas"]
shuffle(l)
a = l[8]
xd = l[:]
xd.pop(8)
xd = [a] + xd
for x, y in zip(l, xd):
    file2write = open(x + "2.0.txt", 'w')
    file2write.write("Elo melo 420")
    file2write.write("Kup prezencik dla: " + y)
    file2write.close()







