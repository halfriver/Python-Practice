# Problem 42: Image Converter
 # take an image and split it into its RBG components
 # make the image greyscale and invert its colors as well

# Original: 8 December 2019
# Edited: 1 December 2020

from PIL import Image

def greyscale(color_tuple):
    color = 0
    for num in range(len(color_tuple)):
        color += color_tuple[num]
    color = int(color/3)
    return((color, color, color))

def invert(color_tuple):
    color = []
    for num in range(len(color_tuple)):
        color.append(int(255 - color_tuple[num]))
    return(tuple(color))

convert = ["red", "green", "blue", "grey", "inv"]
for process in range(len(convert)):
    image = Image.open("inputfiles/P42-kingfishers.jpg")
    pixels = image.load()
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            # split into RGB
            if process <= 2:
                color = [0, 0, 0]
                color[process] = pixels[i,j][process]
                image.putpixel((i, j), tuple(color))
            # greyscale
            elif process == 3:
                image.putpixel((i, j), greyscale(pixels[i,j]))
            # invert colors
            elif process == 4:
                image.putpixel((i, j), invert(pixels[i,j]))
    image.save("outputfiles/P42-kingfishers_" + convert[process] + ".jpg")
        
print("Process completed! Go check out the end results in the outputfiles folder.")
