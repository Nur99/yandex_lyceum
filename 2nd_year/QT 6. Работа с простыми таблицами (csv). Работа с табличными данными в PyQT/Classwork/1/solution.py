f = open('input.bmp', 'rb').read()

new_pallet = f[:54] + bytes([255 - d for d in f[54:]])

res = open('res.bmp', 'wb')
res.write(new_pallet)
res.close()
