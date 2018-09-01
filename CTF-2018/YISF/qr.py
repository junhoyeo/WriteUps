from PIL import Image
import zxing
reader = zxing.BarCodeReader()

# im = Image.open('QR.png') 
# pix = im.load()
# data = []
# kind = []
# for y in range(im.size[0]):
#     for x in range(im.size[1]):
#         pixel = pix[y,x]
#         pixel = (pixel[0], pixel[1], pixel[2])
#         if pixel not in kind:
#             kind.append(pixel) # rgb
#         data.append(pixel)
# print(im.size)
# for i, pixel in enumerate(data):
#     if (pixel[0]>(127/2)): 
#         if pixel in kind:
#             kind.remove(pixel)
#         data[i] = (0, 0, 0)
#     else: data[i] = (255, 255, 255)
# print(kind)
# image = Image.new('RGB', (165, 165))
# image.putdata(data)
# image.save('1.png')
# barcode = reader.decode("1.png")
# print(barcode.raw) # Plz~~!!}

# im = Image.open('QR.png') 
# pix = im.load()
# data = []
# kind = [30, 32, 33, 34, 35, 36, 37, 38, 39, 41, 42, 43, 45, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 66,68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 79, 80, 81, 82, 83, 84, 86, 87, 90, 91, 92, 93, 95, 96, 97, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127]
# for y in range(im.size[0]):
#     for x in range(im.size[1]):
#         pixel = pix[y,x]
#         pixel = (pixel[0], pixel[1], pixel[2])
#         data.append(pixel)
#         # if pixel[0] not in kind:
#         #     kind.append(pixel[0])
# # print(sorted(kind))
# d = []
# for idx, k in enumerate(kind):
#     tmp = data.copy()
#     for i, pixel in enumerate(tmp):
#         # print(pixel)
#         if pixel[0]<(k/2): 
#             tmp[i] = (255, 255, 255)
#         else: tmp[i] = (0, 0, 0)
#     # if data[0] == (0, 0, 0):
#     #     for i, pixel in enumerate(data):
#     #         if pixel[0]== 0: 
#     #             data[i] = (255, 255, 255)
#     #         else:
#     #             data[i] = (0, 0, 0)
#     image = Image.new('RGB', (165, 165))
#     image.putdata(tmp)
#     name = str(idx) + '.png'
#     image.save(name)
#     print('[*] Scanning ' + name)
#     barcode = reader.decode(name)
#     try: print('[!] Data found :' + barcode.raw)
#     except AttributeError: continue

im = Image.open('QR.png') 
pix = im.load()
data = []
for y in range(im.size[0]):
    for x in range(im.size[1]):
        pixel = pix[y,x]
        pixel = (pixel[0], pixel[1], pixel[2])
        data.append(pixel) 
d = ''
for i in data:
    d += str(i[0]&1)
arr = [(int(d[i:i+8], 2), int(d[i:i+8], 2), int(d[i:i+8], 2)) for i in range(0, len(d), 8)]
print (len(arr))
image = Image.new('RGB', (165, 165))
image.putdata(arr)
image.save('lsb-secret.png')

im = Image.open('QR.png') 
pix = im.load()
data = []
for y in range(im.size[0]):
    for x in range(im.size[1]):
        pixel = pix[y,x]
        pixel = (pixel[0], pixel[1], pixel[2])
        data.append(pixel) 
d = ''

def binary(i):
    if i == 0:
        return "0"
    s = ''
    while i:
        if i & 1 == 1:
            s = "1" + s
        else:
            s = "0" + s
        i >>= 1
    return s 

for i in data:
    d += str(binary(i[0])[0:8])
arr = [(int(d[i:i+8], 2), int(d[i:i+8], 2), int(d[i:i+8], 2)) for i in range(0, len(d), 8)]
print (len(arr))
image = Image.new('RGB', (165, 165))
image.putdata(arr)
image.save('msb-secret.png')

# im = Image.open('secret.png') 
# pix = im.load()
# data = []
# for y in range(im.size[0]):
#     for x in range(im.size[0]):
#         pixel = pix[x, y]
#         pixel = (pixel[0], pixel[1], pixel[2])
#         data.append(pixel)
# tmp = data.copy()
# for i, pixel in enumerate(tmp):
#     if (pixel[0]): 
#         tmp[i] = (0, 0, 0)
#     else: tmp[i] = (255, 255, 255)
# image = Image.new('RGB', (165, 165))
# image.putdata(tmp)
# image.save('secret-rec-' + str(offset) + '.png')