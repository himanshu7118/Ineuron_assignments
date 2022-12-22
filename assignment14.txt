1.	What does RGBA stand for?
Ans: RGBA tuples are 4-tuples where the respective tuple components represent red, green, blue, and alpha values for a color.

2.	From the Pillow module, how do you get the RGBA value of any images?
Ans:
 import the Image module from the Pillow library. 
from PIL import Image.
Open any image and get the RAGBAG values. 
img = Image.open('image.png') 
rgba = img.convert(“RGBA”)

3.	What is a box tuple, and how does it work?
Ans: Python Tuple is a collection of objects separated by commas. In some ways, a tuple is similar to a list in terms of indexing, nested objects, and repetition but a tuple is immutable, unlike lists which are mutable.

4.	Use your image and load in notebook then, How can you find out the width and height of an Image object?
Ans: img = Image.open(filepath)
width = img.width
height = img.height

5.	What method would you call to get Image object for a 100×100 image, excluding the lower-left quarter of it?
Ans: from PIL import Image
	Img = Image.open(filepath)
      croppedIm = Img.crop((0,100,0,100))
	croppedIm.save('cropped.png')

6.	After making changes to an Image object, how could you save it as an image file?
Ans: img.save(imagename)

7.	What module contains Pillow’s shape-drawing code?
Ans: ImageDraw

8.	Image objects do not have drawing methods. What kind of object does? How do you get this kind of object?
Ans: from PIL import Image, ImageDraw
  img = Image.open('img_path.png')
  
  draw = ImageDraw.Draw(img)


