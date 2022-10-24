# Author : Manohar Akula
# Date: 10/23/22
# Project - Data Munging Assignment



from xml.dom import minidom
import glob
from matplotlib import image
from matplotlib import pyplot
import matplotlib.pyplot as plt
import os
import matplotlib.patches as patches
import matplotlib
import matplotlib.image as mpimg
from core import convert
import numpy as np
import csv
lut={}
lut["Dirt"] = 0
lut["Water"] = 1
import random


red_pixels_dirt = []
green_pixels_dirt = []
blue_pixels_dirt = []
red_pixels_water = []
green_pixels_water = []
blue_pixels_water = []
def xml_converter(lut):
    for imgpath in glob.glob("data_original/img/*.png"):
        print(imgpath)
        fname = "data_original/xmls/"+imgpath.split("\\")[1].split(".")[0] +".xml" 
        print(imgpath)
        img = mpimg.imread(imgpath)
        R_channel = img[:,:,0]
        G_channel = img[:,:,1]
        B_channel = img[:,:,2]
        print(R_channel.dtype)

        fig, ax = plt.subplots()
        plt.axis('off')
        ax.imshow(img)
        print(fname)
        if os.path.isfile(fname): 
            xmldoc = minidom.parse(fname)
            fname_out = (fname[:-4] + '.txt')
            with open(fname_out, "w") as f:
                itemlist = xmldoc.getElementsByTagName('object')
                size = xmldoc.getElementsByTagName('size')[0]
                width = int((size.getElementsByTagName('width')[0]).firstChild.data)
                height = int((size.getElementsByTagName('height')[0]).firstChild.data)

                for item in itemlist:
                    # get class label
                    classid = (item.getElementsByTagName('name')[0]).firstChild.data
                    if classid in lut:
                        label_str = str(lut[classid])
                    else:
                        label_str = "-1"
                        print("warning: label '%s' not in look-up table" % classid)

                    # get bbox coordinates
                    xmin = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('xmin')[0]).firstChild.data
                    ymin = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('ymin')[0]).firstChild.data
                    xmax = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('xmax')[0]).firstChild.data
                    ymax = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('ymax')[0]).firstChild.data
                    b = [float(xmin), float(xmax), float(ymin), float(ymax)]
                    x,y,w,h = convert(b)
                    rect = patches.Rectangle((x, y), w, h, linewidth=1, edgecolor='r', facecolor='none')
                    ax.add_patch(rect)
                    ax.text(x,y, classid)

                    if random.randint(0, 20) ==  2:
                        if classid =="Water":
                            fig2, ax2 = plt.subplots()
                            plt.axis('off')
                            ax2.imshow(img[int(ymin):int(ymax) , int(xmin):int(xmax)])
                            red_pixels_water.append(R_channel[int(ymin):int(ymax) , int(xmin):int(xmax)])
                            blue_pixels_water.append(B_channel[int(ymin):int(ymax) , int(xmin):int(xmax)])
                            green_pixels_water.append(G_channel[int(ymin):int(ymax) , int(xmin):int(xmax)])
                            fig2.savefig("data_preprocessed\\cropped_water\\"+imgpath.split("\\")[1].split(".")[0] +".png" , dpi=90, bbox_inches='tight', pad_inches=0)
                        else:
                            fig2, ax2 = plt.subplots()
                            plt.axis('off')
                            red_pixels_dirt.append(R_channel[int(ymin):int(ymax) , int(xmin):int(xmax)])
                            blue_pixels_dirt.append(B_channel[int(ymin):int(ymax) , int(xmin):int(xmax)])
                            green_pixels_dirt.append(G_channel[int(ymin):int(ymax) , int(xmin):int(xmax)])
                            ax2.imshow(img[int(ymin):int(ymax) , int(xmin):int(xmax)])
                            fig2.savefig("data_preprocessed\\cropped_dirt\\"+imgpath.split("\\")[1].split(".")[0] +".png" , dpi=90, bbox_inches='tight', pad_inches=0)
        fig.savefig("data_preprocessed\\detections\\"+imgpath.split("\\")[1].split(".")[0] +".png" , dpi=90, bbox_inches='tight', pad_inches=0)
        plt.close(fig)
        print("wrote %s" % fname_out)
    with open("data_preprocessed\\cropped_water\\red_pixels.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(red_pixels_water)
    with open("data_preprocessed\\cropped_water\\blue_pixels.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(blue_pixels_water)
    with open("data_preprocessed\\cropped_water\\green_pixels.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(green_pixels_water)
    with open("data_preprocessed\\cropped_dirt\\red_pixels.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(red_pixels_dirt)
    with open("data_preprocessed\\cropped_dirt\\blue_pixels.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(blue_pixels_dirt)
    with open("data_preprocessed\\cropped_dirt\\green_pixels.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(green_pixels_dirt)

xml_converter(lut)