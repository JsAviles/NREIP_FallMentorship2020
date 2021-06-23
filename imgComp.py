#######################################################################################
#  Name : Jesus 'Sebastian' Aviles                                                    #
#  File : Source code for simulation of run-length encoding to compress image file    #                                                 
#  Date : 12/29/2020                                                                  #
#                                                                                     #
#  Produced for the NREIP Fall Engagement project in 2020                             #
#######################################################################################

import numpy as np
from PIL import Image

np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)

#########################################################################
#                   Declare variables for file ouput                    #
#########################################################################

uncompressedF = open('NREIP_uncompF.txt', 'w+')
compressedF = open('NREIP_compF.txt', 'w+')
img = Image.open('stem.jpg', 'r')
width, height = img.size
px_c_values = np.asarray(img)
eoa = (width * height * 3)

#########################################################################
#               Save uncompressed image from numpy array                #
#########################################################################

newImage = Image.fromarray(px_c_values)
newImage.save('NREIP_uncompressed_image.tiff')

#########################################################################
#          Write raw data out to text file for visualization            #
#########################################################################

byteCtr = 0
#iterate through np array
for elem in px_c_values:
    for pixel in elem:
        for color in pixel:
            uncompressedF.write(str(color))
        byteCtr += 1
    if (byteCtr * 3) != eoa:
        uncompressedF.write("\n")
    else:
        print("_________________________________________________________\n\nFinished writing to uncompressedF.txt...\n")

#########################################################################
#                    Run-Length encoding algorithm                      #
#########################################################################

row = 0
cAr = []
#row/width -- changed range(1056 to 816)
for row in range(height):

    #declare row List to append new rl bytes and color bytes to
    rowAr = []
    col = 0
    #col/height  -- changed 815 to 1055
    while (col < (width-1)):

        #set temp to the first pixel in the run-length
        temp = px_c_values[row][col]
        rLength = 0
        #iterate while the proceeding pixels are equal 
        while((col < (width-1)) & np.array_equal(temp, px_c_values[row][col])):
            rLength += 1
            col += 1
        
        #upon exit of while loop, append rLength value to new compressed array then add color list
        rowAr.append(rLength)
        rowAr.append(temp)

    #append the rowAr once the full pixel row has been compressed with the runLength byte
    cAr.append(rowAr)
#end For loop

#########################################################################
#                    Write data out to text file                        #
#########################################################################
rowCtr = 0
ctr = 0
for elem in cAr:
    for byte in elem:
        #check if ctr is pointing to an odd number which will indiciate the position of a color "list"
        if (ctr % 2 != 0):
            for value in byte:
                compressedF.write(str(value))
        else:
            compressedF.write(str(byte)) 
        ctr += 1
    rowCtr += 1
    if rowCtr != height:
        compressedF.write("\n")

#########################################################################
#                        Compression analysis                           #
#########################################################################

byteCtr = (byteCtr*3)
bytes = ((ctr/2) + ((ctr/2)*3))

#convert list to numpy array
arr = np.array(cAr)
compSize = 0

#iterate through np array
for row in arr:
    for col in row:
        if type(col) == int:
            compSize += 1
        else:
            compSize += col.size
#arr.save('NREIP_compressed_image.tiff')

print("Image (HeightxWidth): (" + str(height) + "x"+ str(width) + ")")
print("Image shape: " + str(px_c_values.shape) + "\nImage mode: " + str(img.mode) + "\nUncompressed byte size = " + str(px_c_values.size))
print("Compressed byte size = " + str(compSize))
print("Compressed percentage = {:.2f}".format((100 - ((compSize/(byteCtr))*100))) + "%\n")

#########################################################################
#                    Decompress and re-create Image                     #
#########################################################################

print("Decompressing new Image array...")

lenCtr = 0
dcAr = []
for row in arr:
    rowAr = []
    for col in row:
        #Set Run Length Counter
        if type(col) == int:
            lenCtr = col
        else:
            for i in range(lenCtr):
                rowAr.append(col)
    dcAr.append(rowAr)

#convert decompressed array to numpy array and create/save new image
dcImage = np.array(dcAr)
newcompImage = Image.fromarray(dcImage)
newcompImage.save('NREIP_compressed_image.tiff')

print("\nFinished writing to uncompressedF.txt...")
print("_________________________________________________________\n")

# Close open files
uncompressedF.close()
compressedF.close()

#########################################################################
#                            End of Program                             #
#########################################################################