import os
from pyzbar.pyzbar import decode
from PIL import Image
res = ''
filenames = sorted([int(name.replace('.png', '')) for name in os.listdir('./qrs/')])
for filename in filenames:
	if qr:=decode(Image.open('./qrs/'+str(filename)+'.png')):
		res += qr[0].data.decode()
        else: print(f'error with file {filename}')
print(res)
