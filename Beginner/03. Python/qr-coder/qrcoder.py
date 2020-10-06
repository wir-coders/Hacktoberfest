import pyqrcode, sys
data = sys.argv[1]
for ch in enumerate(data):
	qrch = pyqrcode.create(ch[1])
	qrch.png('./qrs/'+str(ch[0])+'.png', scale=6)
