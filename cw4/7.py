i = input()

s = 0

maax = 0

miin = 0

while i != "!":

    if (int(i) >= 150) and (int(i) <= 190):

        if (miin == 0) and (maax == 0):

            maax = int(i)

            miin = int(i)

        s += 1

        if maax < int(i):

            maax = int(i)

        if miin > int(i):

            miin = int(i)

    i = input()

print(s)

print(str(miin) + " " + str(maax))
