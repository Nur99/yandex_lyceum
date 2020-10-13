def reverse():
    inp = open("input.dat", mode="rb")
    out = open("output.dat", mode="wb")
    out.write(bytes(inp.read())[::-1])
    inp.close()
    out.close()
