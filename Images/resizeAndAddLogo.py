#!/usr/bin/python3

import os
from PIL import Image

SQUARE_FIt_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

#Loop over files in current directory
os.makedirs('withLogo', exist_ok=True)
for filename in os.listdir('.'):
    if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg')) or filename == LOGO_FILENAME:
        continue

    im = Image.open(filename)
    width, height = im.size

    #Check if images needs to be resized.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        #calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        #Resize the image
        print('Resizing %s...', % (filename))
        im = im.resize((width, height))

        #Add the logo
        print('Adding logo to %s...' % (filename))
        im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
        im.save(os.path.join('withLogo', filename))
