from PIL import Image

flag = "INXWIZLGMVZXIQ2UIZ5TKMLNOBWDGX3MONRF6NJXGNTTAX3GOR3X2==="
data = "".join(format(ord(i), '08b') for i in flag)

img = Image.open('original.png')
pixels = img.load()

index = 0

for j in range(img.height):
    for i in range(img.width):
        pixel = list(pixels[i, j])
        for k in range(3):
            if index < len(data):
                pixel[k] = pixel[k] & ~1 | int(data[index])
                index += 1
        pixels[i, j] = tuple(pixel)
        if index >= len(data):
            break

img.save('chall.png')
