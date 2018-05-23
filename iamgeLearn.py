from PIL import Image

class ImageLearn:
	def __init__(self):
		# self.zoomImage()
		self.testAssert()
	def zoomImage(self):
		im = Image.open('1.jpg')
		w,h = im.size
		print(w,h)
		im.thumbnail((w//2 ,h//2))
		# im.save('2.jpg','jpeg')

		im.save()
		print()
	def testAssert(self):
		i = 4
		assert i > 3,'i<3'
ImageLearn()