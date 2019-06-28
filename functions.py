import os
import numpy as np
import cv2
from scipy import ndimage


# Discordify an image
def discordify(image):
    pass


# Create original work
def original(category):
    # Create database

    imgRepoDir = "dir"
    databaseDir = "dir"
    imgSize = 128

    colorImgs = []

    for file in os.listdir(imgRepoDir):
        path = imgRepoDir + "/" + file
        img = ndimage.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        # Crop center of image
        height = img.shape[0]
        width = img.shape[1]
        if width > height:
            offs = (width - height) / 2
            img = img[:, offs:offs + height, :]
        elif height > width:
            offs = (height - width) / 2
            img = img[offs:offs + width, :, :]

        # Scale all images
        img = cv2.resize(img, (imgSize, imgSize), interpolation=cv2.INTER_AREA)

        # Add to list
        colorImgs.append(np.transpose(img, (2, 0, 1)))

    colorImgs = np.stack(colorImgs, axis=0)
    np.save(databaseDir + '/color' + str(imgSize) + '.npy', colorImgs)

    if category == 'fanart':
        pass
    elif category == 'merch':
        pass
    elif category == 'emoji':
        pass
    elif category == 'story':
        pass
